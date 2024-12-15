w### **Role-Based Access Control (RBAC) - Key Points**


Compared to ACL, RBAC allows for abstraction through roles, while ACLs are directly mapping users to policies
Ease of management, and scalability over ACLs
The changes to role policies need to be checked and ensured correct, as single change now affects big amount of users.
Mining
* Approached by figuring out the differences in policies between the mentioned users. Identified overlaps between user permissions:
	* The four roles has been identified: User, Power User, Manager, Technician
	* Power user has overlap with users: print, queue
	* Manager has overlap with Power User: Print, Queue, Top QUeue, restart
	* Manager has overlap with Technician: Start, Stop, Restart, Status, Red Configu, Set Config
* These overlaps has been taken and a hierarchy has been identified, that ensures that each role has correct policies after inheriting policies of its children. These logical groupings also satisfies the names in the language, as power user should be allowed to do more as ordinary user
* Some of the conflicts has been identified, for example between power user and technician: Technician cannot print and queue, and has more access to more technical policies. This is why teh technician is on the same level as power user, and allow manage to inherit its policies.
* Manager is at the root of the hierarchy, because of its managing permissions that allow all operations to ocurr.
* Role names mentioned in the assignment were also a nice hint, as it is expected from the lnaguage that Power User will have more policies than user
* The roles have a hierarchy, meaning that the parent contains all policies that its children have
* A discrepancy have been identified between Technician and Power User. Initially we thought the role hierarchy will always be that each parent has only one children, however we have identified that not all policies included in technician are also in power user (file printing was missing in technician). Therefore we have decided to create two different roles on the same level, and add them as children to manager (Alice), as she can perform all operations

Diagram:
![[Pasted image 20241122130603.png]]

Implementation mechanism: 
* 3 tables has been created:
	* role_policies containting poplicies assigned to the given role. centrally managed policies
	* role_hierarchy containing relationsgips between parent and children. Allows for ingeritance through parent-child relationships
	* user_roles containing mapping between users and its roles for consistency enforcement 
* Normalized architecture, that allows for data without redundancy, and ensure single source of truth.
* The goal of this implementation was that the policies of a specific role are defined ONLY on one place, ensuring that a single change can affect all user that has assigned given role. This is the biggest benefit or RBAC, as we have only one place where a change is required, otherwise it could happend that on each redundant definition, a change is required. 
* We knew that it will be required from parent to lookup its children, therefore we have decided to opt in for storing parent -> children relationships in teh database. This allowed us to efficiently check the parents children. 
* The implementation of the RBAC check is as follows: 


```
private void addChildRolesAccess(String role, List<String> accessControlList) {  
    for (String childRole : hierarchy.getOrDefault(role, Collections.emptyList())) {  
        accessControlList.addAll(rolePolicies.get(childRole));  
        addChildRolesAccess(childRole, accessControlList);  
    }  
}  
  
@Override  
public List<String> getAccess(String subject) {  
    String role = userRoles.get(subject);  
    if (role == null) {  
        return Collections.emptyList(); // No role assigned  
    }  
    List<String> accessControlList = new ArrayList<>(rolePolicies.getOrDefault(role, Collections.emptyList()));  
    addChildRolesAccess(role, accessControlList);  
    return accessControlList;  
}
```
We have used recursion to ensure all children are checked, even children of children. The recursion ends when a current parent has no more children. It appends teh policies to access control list until this ending case.
Recursion balances efficiency and simplicity of the code.
* The database allows for efficient querying, and is loaded when teh server starts. However, it would be more benficial for the server to access db values eacah time a requests come, not only when run, to ensure up-to-date information. We have decided to go with this approach as teh assignment have put requirement only on the information being accessed on server run.
* The design approach allowed for:
* Scalability: No need to add all policies redundandtly to the given user, only role can be assigned. Supports larget organizations. Changes affects multiple users with the assigned role
* Flexibility: Doesnt require user level changes, allows for role reassignment during changes in the organization
* Security: The roles are source of truth for policies, and therefore it is more readable and easier to check policies of users. If po;icies would be spocified per user, each user would need to be checked whether he/she does not hae more permissions than required. Auditability is increased.



1. **Role Mining Results:**
    
    - **Role Identification:**
        - Alice (Manager): Full access rights.
        - Bob (Technician): Operational rights (start/stop/restart server, inspect/modify service parameters).
        - Cecilia (Power User): File printing, queue management, and restart server.
        - Ordinary Users: Limited rights (file printing and display queue).
    - **Role Hierarchy:**
        - Define a hierarchy where roles are inherited:
            - Alice (Manager) > Cecilia (Power User) > Bob (Technician) > Ordinary Users.
2. **Implementation of RBAC Mechanism:**
    
    - **Policy Specification:**
        - External policy files to define role-permission mappings.
        - Syntax of the RBAC policy uses declarative rules, e.g., JSON, XML, or simple text-based mappings.
    - **Dynamic Role Assignment:**
        - Mapping user roles dynamically during authentication based on their credentials.
    - **Permission Enforcement:**
        - Ensure only authorized methods are invoked based on role permissions.
        - Real-time role validation for every request.
3. **Design Motivations:**
    
    - **Scalability:** Role hierarchy simplifies administration as roles are easier to manage than individual permissions.
    - **Flexibility:** External policy files make it easier to adapt to organizational changes.
    - **Security:** Explicit separation of privileges reduces the risk of unauthorized actions.
4. **Syntax for Policy Specification:**
    
    - Provide an example of a role-policy mapping file:
        
        json
        
        Copy code
        
        `{   "roles": {     "Manager": ["print", "queue", "topQueue", "start", "stop", "restart", "status", "readConfig", "setConfig"],     "Technician": ["start", "stop", "restart", "status", "readConfig", "setConfig"],     "PowerUser": ["print", "queue", "topQueue", "restart"],     "OrdinaryUser": ["print", "queue"]   } }`
        
5. **Diagram to Support Explanation:**
    
    - Include a diagram illustrating the role hierarchy and permission assignment.

---

### **Changes in the Policy - Key Points**

1. **Organizational Changes:**
    
    - **Bob Leaves:** Reassign Bob’s Technician role to George.
    - **New Employees:**
        - Henry: Assigned as an Ordinary User.
        - Ida: Assigned the Power User role.
2. **Policy Update Reflection:**
    
    - **Access Control List (ACL):**
        - Modify the access list manually to update user permissions.
        - Highlight limitations like manual effort and risk of errors.
    - **RBAC:**
        - Update role assignments in the external policy file, ensuring minimal effort.
        - Explain how the policy syntax allows smooth transitions:
            
            json
            
            Copy code
            
            `{   "users": {     "George": "Technician",     "Henry": "OrdinaryUser",     "Ida": "PowerUser"   } }`
            
3. **Comparison of ACL vs. RBAC for Policy Updates:**
    
    - **Ease of Updates:**
        - ACL: Tedious and error-prone as each user-policy mapping needs updating.
        - RBAC: Simplified by modifying role assignments.
    - **Scalability:**
        - RBAC is more scalable due to the abstraction provided by roles.
    - **Security Risks:**
        - ACL increases risk of misconfiguration during updates.
4. **Reflections on Management Support:**
    
    - RBAC simplifies administrative overhead and supports dynamic organizational structures better.
    - ACL might still be preferred for small, static systems due to its simplicity.
5. **Lessons Learned:**
    
    - Emphasize the importance of external policy files and role-based abstractions in maintaining flexible and secure systems.
