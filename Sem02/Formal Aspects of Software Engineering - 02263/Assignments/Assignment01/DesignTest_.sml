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
    
structure RT_x_5 =
    struct
        type t = RT_s_1.t * RT_s_2.t;
        
        fun equ (x:t, y:t) = RT_s_1.equ(#1 x, #1 y) andalso 
                             RT_s_2.equ(#2 x, #2 y);
        
        fun toString (x:t) = "(" ^
                             (RT_s_1.toString(#1 x )) ^ "," ^
                             (RT_s_2.toString(#2 x )) ^
                             ")";
        
        fun toStringSafe x = toString(x())
          handle RSL.RSL_exception s => (RSL.inc_exception_count(); s);
        
        fun typeToString () = "(" ^
                              (RT_s_1.typeToString ()) ^ " >< " ^
                              (RT_s_2.typeToString ()) ^
                              ")";
    end;
    
structure DesignTest =
    struct
        type Person_ = RT_Text.t;
        
        type Family_ = RT_s_1.t;
        
        type Families_ = RT_s_2.t;
        
        type Table_ = RT_s_1.t;
        
        type Plan_ = RT_s_2.t;
        
        fun reqAllFamilyMembersAreSeated'3781_ (p'3802_, fs'3805_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (56, 13)); ((RT_s_2.R_all (fn (f'3852_:RT_s_1.t) => ((RT_s_1.R_all (fn (person'38BA_:RT_Text.t) => ((RT_s_2.R_exists (fn (t'3925_:RT_s_1.t) => RT_s_1.R_mem (person'38BA_, t'3925_)) (p'3802_)))) (f'3852_)))) (fs'3805_))));
        
        fun areRelatives'2719_ (p1'278A_, p2'278E_, fs'2792_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (14, 11)); ((RT_s_2.R_exists (fn (f'27EB_:RT_s_1.t) => (RT_s_1.R_mem (p1'278A_, f'27EB_)) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (14, 58)); RT_s_1.R_mem (p2'278E_, f'27EB_))) (fs'2792_))));
        
        fun reqNoEmptyTables'35F1_ p'3666_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (52, 11)); ((RT_s_2.R_all (fn (t'36C0_:RT_s_1.t) => (RSL.C_not RT_s_1.equ) (t'36C0_, RT_s_1.R_fromList [])) (p'3666_))));
        
        fun reqNoEmptyFamilies'2A9D_ fs'2B14_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (23, 11)); ((RT_s_2.R_all (fn (f'2B6C_:RT_s_1.t) => (RSL.C_not RT_s_1.equ) (f'2B6C_, RT_s_1.R_fromList [])) (fs'2B14_))));
        
        fun reqNoDuplicateFamilyMembers'2C2D_ fs'2CAD_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (27, 11)); ((RT_s_2.R_all (fn (f1'2CFC_:RT_s_1.t) => ((RT_s_2.R_all (fn (f2'2D62_:RT_s_1.t) => not ((RSL.C_not RT_s_1.equ) (f1'2CFC_, f2'2D62_)) orelse (RT_s_1.equ (RT_s_1.R_inter (f1'2CFC_, f2'2D62_), RT_s_1.R_fromList []))) (fs'2CAD_)))) (fs'2CAD_))));
        
        fun isWellformed'290D_ fs'297E_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (19, 11)); ((((reqNoEmptyFamilies'2A9D_) (fs'297E_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (19, 38)); ((reqNoDuplicateFamilyMembers'2C2D_) (fs'297E_)))));
        
        fun reqNoFamilyMembersSeatedTogether'3141_ (p'31C6_, fs'31C9_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (40, 11)); ((RT_s_2.R_all (fn (t'3210_:RT_s_1.t) => ((RT_s_1.R_all (fn (p1'3276_:RT_Text.t) => ((RT_s_1.R_all (fn (p2'32DC_:RT_Text.t) => not ((RSL.C_not RT_Text.equ) (p1'3276_, p2'32DC_)) orelse (not (((areRelatives'2719_) (p1'3276_, p2'32DC_, fs'31C9_))))) (t'3210_)))) (t'3210_)))) (p'31C6_))));
        
        fun reqEachFamilyMemberSeatedOnce'3399_ (p'341B_, fs'341E_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (46, 13)); ((RT_s_2.R_all (fn (f'346A_:RT_s_1.t) => ((RT_s_1.R_all (fn (person'34D2_:RT_Text.t) => ((RT_s_2.R_exists1 (fn (t'353E_:RT_s_1.t) => RT_s_1.R_mem (person'34D2_, t'353E_)) (p'341B_)))) (f'346A_)))) (fs'341E_))));
        
        fun isCorrectPlan'2E85_ (p'2EF7_, fs'2EFA_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (33, 11)); ((((reqNoFamilyMembersSeatedTogether'3141_) (p'2EF7_, fs'2EFA_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (34, 12)); (((reqEachFamilyMemberSeatedOnce'3399_) (p'2EF7_, fs'2EFA_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (35, 12)); (((reqNoEmptyTables'35F1_) (p'2EF7_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (36, 12)); ((reqAllFamilyMembersAreSeated'3781_) (p'2EF7_, fs'2EFA_)))))));
        
        fun combine'14B9_ (table'1525_, plan'152C_) = (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (23, 5)); (if RT_s_1.equ (table'1525_, RT_s_1.R_fromList []) then (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (24, 26)); plan'152C_) else (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (26, 9)); if RT_s_2.equ (plan'152C_, RT_s_2.R_fromList []) then (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (27, 11)); RT_s_2.R_fromList ([table'1525_])) else (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (29, 11)); RT_s_2.R_union (RT_s_2.R_fromList ([table'1525_]), plan'152C_)))));
        
        fun allEmpty'10D1_ families'113E_ = (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (13, 5)); ((RT_s_2.R_all (fn (f'1203_:RT_s_1.t) => RT_s_1.equ (f'1203_, RT_s_1.R_fromList [])) (families'113E_))));
        
        fun interleave'1B5D_ families'1BCC_ = (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (40, 5)); (if ((allEmpty'10D1_) (families'1BCC_)) then (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (42, 9)); RT_s_2.R_fromList []) else (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (44, 7)); ((combine'14B9_) (, ((interleave'1B5D_) ()))))));
        
        fun plan'20D5_ fs'213E_ = (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (53, 17)); if not(((isWellformed'290D_) (fs'213E_))) then raise RSL.RSL_exception ("./Design.rsl:54:9: Precondition of plan" ^ "(" ^ RT_s_2.toString fs'213E_ ^ ")" ^ " not satisfied") else ((interleave'1B5D_) (fs'213E_)));
        
        val p3'389_ = RT_Text.fromLit "Erik";
        
        val p1'2C1_ = RT_Text.fromLit "Elisabeth";
        
        val duplicatedF5'89D_ = RT_s_1.R_fromList ([p1'2C1_, p3'389_]);
        
        val p2'325_ = RT_Text.fromLit "Lillian";
        
        val f2'771_ = RT_s_1.R_fromList ([p2'325_, p3'389_]);
        
        val duplicatedFamilies'9C9_ = RT_s_2.R_fromList ([f2'771_, duplicatedF5'89D_]);
        
        val p4'3ED_ = RT_Text.fromLit "Frederik";
        
        val p11'6A9_ = RT_Text.fromLit "Pernille";
        
        val p7'519_ = RT_Text.fromLit "Lotte";
        
        val p10'645_ = RT_Text.fromLit "Jacob";
        
        val p8'57D_ = RT_Text.fromLit "Torsten";
        
        val p9'5E1_ = RT_Text.fromLit "Camilla";
        
        val f4'839_ = RT_s_1.R_fromList ([p7'519_, p8'57D_, p9'5E1_, p10'645_, p11'6A9_]);
        
        val f1'70D_ = RT_s_1.R_fromList ([p1'2C1_]);
        
        val p6'4B5_ = RT_Text.fromLit "Anne";
        
        val p5'451_ = RT_Text.fromLit "Henrik";
        
        val f3'7D5_ = RT_s_1.R_fromList ([p4'3ED_, p5'451_, p6'4B5_]);
        
        val families'901_ = RT_s_2.R_fromList ([f1'70D_, f2'771_, f3'7D5_, f4'839_]);
        
        val emptyFamilies'965_ = RT_s_2.R_fromList ([RT_s_1.R_fromList []]);
        
    end;
    
open DesignTest;

RSL.print_load_errs();
RSL.set_time();
R_coverage.init();
(R_coverage.mark(RT_Text.fromLit "./Design.rsl", (53, 17), (55, 3));
R_coverage.mark(RT_Text.fromLit "./Design.rsl", (44, 7), (49, 7));
R_coverage.mark(RT_Text.fromLit "./Design.rsl", (42, 9), (43, 10));
R_coverage.mark(RT_Text.fromLit "./Design.rsl", (40, 5), (50, 6));
R_coverage.mark(RT_Text.fromLit "./Design.rsl", (13, 5), (15, 6));
R_coverage.mark(RT_Text.fromLit "./Design.rsl", (29, 11), (30, 9));
R_coverage.mark(RT_Text.fromLit "./Design.rsl", (27, 11), (28, 12));
R_coverage.mark(RT_Text.fromLit "./Design.rsl", (26, 9), (31, 7));
R_coverage.mark(RT_Text.fromLit "./Design.rsl", (24, 26), (25, 10));
R_coverage.mark(RT_Text.fromLit "./Design.rsl", (23, 5), (32, 6));
R_coverage.mark(RT_Text.fromLit "./Basics.rsl", (36, 12), (36, 47));
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
(RSL.C_output "[t1] " RT_Bool.toStringSafe (fn _ => RT_Bool.equ (((isWellformed'290D_) (families'901_)), true)));

(RSL.C_output "[t2] " RT_Bool.toStringSafe (fn _ => RT_Bool.equ (((isWellformed'290D_) (emptyFamilies'965_)), false)));

(RSL.C_output "[t3] " RT_Bool.toStringSafe (fn _ => RT_Bool.equ (((isWellformed'290D_) (duplicatedFamilies'9C9_)), false)));

RSL.print_error_count();
R_coverage.save_marked();
