structure RT_Text = RT_Text;

structure RT_s_1 = RT_Set(structure Elem = RT_Text);

structure RT_s_2 = RT_Set(structure Elem = RT_s_1);

structure RT_x_3 =
    struct
        type t = RT_Text.t * RT_Text.t * RT_s_2.t;
        
        fun equ (x:t, y:t) = RT_Text.equ(#1 x, #1 y) andalso 
                             RT_Text.equ(#2 x, #2 y) andalso 
                             RT_s_2.equ(#3 x, #3 y);
        
        fun toString (x:t) = "(" ^
                             (RT_Text.toString(#1 x )) ^ "," ^
                             (RT_Text.toString(#2 x )) ^ "," ^
                             (RT_s_2.toString(#3 x )) ^
                             ")";
        
        fun toStringSafe x = toString(x())
          handle RSL.RSL_exception s => (RSL.inc_exception_count(); s);
        
        fun typeToString () = "(" ^
                              (RT_Text.typeToString ()) ^ " >< " ^
                              (RT_Text.typeToString ()) ^ " >< " ^
                              (RT_s_2.typeToString ()) ^
                              ")";
    end;
    
structure RT_Bool = RT_Bool;

structure RT_x_4 =
    struct
        type t = RT_s_2.t * RT_s_2.t;
        
        fun equ (x:t, y:t) = RT_s_2.equ(#1 x, #1 y) andalso 
                             RT_s_2.equ(#2 x, #2 y);
        
        fun toString (x:t) = "(" ^
                             (RT_s_2.toString(#1 x )) ^ "," ^
                             (RT_s_2.toString(#2 x )) ^
                             ")";
        
        fun toStringSafe x = toString(x())
          handle RSL.RSL_exception s => (RSL.inc_exception_count(); s);
        
        fun typeToString () = "(" ^
                              (RT_s_2.typeToString ()) ^ " >< " ^
                              (RT_s_2.typeToString ()) ^
                              ")";
    end;
    
structure Requirements =
    struct
        type Person_ = RT_Text.t;
        
        type Family_ = RT_s_1.t;
        
        type Families_ = RT_s_2.t;
        
        type Table_ = RT_s_1.t;
        
        type Plan_ = RT_s_2.t;
        
        fun reqAllFamilyMembersAreSeated'19D1_ (p'1A52_, fs'1A55_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (56, 13)); ((RT_s_2.R_all (fn (f'1AA2_:RT_s_1.t) => ((RT_s_1.R_all (fn (person'1B0A_:RT_Text.t) => ((RT_s_2.R_exists (fn (t'1B75_:RT_s_1.t) => RT_s_1.R_mem (person'1B0A_, t'1B75_)) (p'1A52_)))) (f'1AA2_)))) (fs'1A55_))));
        
        fun areRelatives'969_ (p1'9DA_, p2'9DE_, fs'9E2_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (14, 11)); ((RT_s_2.R_exists (fn (f'A3B_:RT_s_1.t) => (RT_s_1.R_mem (p1'9DA_, f'A3B_)) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (14, 58)); RT_s_1.R_mem (p2'9DE_, f'A3B_))) (fs'9E2_))));
        
        fun reqNoEmptyTables'1841_ p'18B6_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (52, 11)); ((RT_s_2.R_all (fn (t'1910_:RT_s_1.t) => (RSL.C_not RT_s_1.equ) (t'1910_, RT_s_1.R_fromList [])) (p'18B6_))));
        
        fun reqNoEmptyFamilies'CED_ fs'D64_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (23, 11)); ((RT_s_2.R_all (fn (f'DBC_:RT_s_1.t) => (RSL.C_not RT_s_1.equ) (f'DBC_, RT_s_1.R_fromList [])) (fs'D64_))));
        
        fun reqNoDuplicateFamilyMembers'E7D_ fs'EFD_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (27, 11)); ((RT_s_2.R_all (fn (f1'F4C_:RT_s_1.t) => ((RT_s_2.R_all (fn (f2'FB2_:RT_s_1.t) => not ((RSL.C_not RT_s_1.equ) (f1'F4C_, f2'FB2_)) orelse (RT_s_1.equ (RT_s_1.R_inter (f1'F4C_, f2'FB2_), RT_s_1.R_fromList []))) (fs'EFD_)))) (fs'EFD_))));
        
        fun isWellformed'B5D_ fs'BCE_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (19, 11)); ((((reqNoEmptyFamilies'CED_) (fs'BCE_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (19, 38)); ((reqNoDuplicateFamilyMembers'E7D_) (fs'BCE_)))));
        
        fun reqNoFamilyMembersSeatedTogether'1391_ (p'1416_, fs'1419_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (40, 11)); ((RT_s_2.R_all (fn (t'1460_:RT_s_1.t) => ((RT_s_1.R_all (fn (p1'14C6_:RT_Text.t) => ((RT_s_1.R_all (fn (p2'152C_:RT_Text.t) => not ((RSL.C_not RT_Text.equ) (p1'14C6_, p2'152C_)) orelse (not (((areRelatives'969_) (p1'14C6_, p2'152C_, fs'1419_))))) (t'1460_)))) (t'1460_)))) (p'1416_))));
        
        fun reqEachFamilyMemberSeatedOnce'15E9_ (p'166B_, fs'166E_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (46, 13)); ((RT_s_2.R_all (fn (f'16BA_:RT_s_1.t) => ((RT_s_1.R_all (fn (person'1722_:RT_Text.t) => ((RT_s_2.R_exists1 (fn (t'178E_:RT_s_1.t) => RT_s_1.R_mem (person'1722_, t'178E_)) (p'166B_)))) (f'16BA_)))) (fs'166E_))));
        
        fun isCorrectPlan'10D5_ (p'1147_, fs'114A_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (33, 11)); ((((reqNoFamilyMembersSeatedTogether'1391_) (p'1147_, fs'114A_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (34, 12)); (((reqEachFamilyMemberSeatedOnce'15E9_) (p'1147_, fs'114A_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (35, 12)); (((reqNoEmptyTables'1841_) (p'1147_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (36, 12)); ((reqAllFamilyMembersAreSeated'19D1_) (p'1147_, fs'114A_)))))));
        
        ;
        
    end;
    
open Requirements;

RSL.print_load_errs();
RSL.set_time();
R_coverage.init();
(R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (36, 12), (36, 47));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (35, 12), (36, 47));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (34, 12), (36, 47));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (33, 11), (36, 48));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (46, 13), (48, 70));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (40, 11), (42, 87));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (19, 38), (19, 69));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (19, 11), (19, 70));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (27, 11), (28, 76));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (23, 11), (23, 50));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (52, 11), (52, 48));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (14, 58), (14, 67));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (14, 11), (14, 68));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (56, 13), (59, 7)));
RSL.print_error_count();
R_coverage.save_marked();
