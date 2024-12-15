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
    
structure Design =
    struct
        type Person_ = RT_Text.t;
        
        type Family_ = RT_s_1.t;
        
        type Families_ = RT_s_2.t;
        
        type Table_ = RT_s_1.t;
        
        type Plan_ = RT_s_2.t;
        
        fun reqAllFamilyMembersAreSeated'28A9_ (p'292A_, fs'292D_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (56, 13)); ((RT_s_2.R_all (fn (f'297A_:RT_s_1.t) => ((RT_s_1.R_all (fn (person'29E2_:RT_Text.t) => ((RT_s_2.R_exists (fn (t'2A4D_:RT_s_1.t) => RT_s_1.R_mem (person'29E2_, t'2A4D_)) (p'292A_)))) (f'297A_)))) (fs'292D_))));
        
        fun areRelatives'1841_ (p1'18B2_, p2'18B6_, fs'18BA_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (14, 11)); ((RT_s_2.R_exists (fn (f'1913_:RT_s_1.t) => (RT_s_1.R_mem (p1'18B2_, f'1913_)) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (14, 58)); RT_s_1.R_mem (p2'18B6_, f'1913_))) (fs'18BA_))));
        
        fun reqNoEmptyTables'2719_ p'278E_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (52, 11)); ((RT_s_2.R_all (fn (t'27E8_:RT_s_1.t) => (RSL.C_not RT_s_1.equ) (t'27E8_, RT_s_1.R_fromList [])) (p'278E_))));
        
        fun reqNoEmptyFamilies'1BC5_ fs'1C3C_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (23, 11)); ((RT_s_2.R_all (fn (f'1C94_:RT_s_1.t) => (RSL.C_not RT_s_1.equ) (f'1C94_, RT_s_1.R_fromList [])) (fs'1C3C_))));
        
        fun reqNoDuplicateFamilyMembers'1D55_ fs'1DD5_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (27, 11)); ((RT_s_2.R_all (fn (f1'1E24_:RT_s_1.t) => ((RT_s_2.R_all (fn (f2'1E8A_:RT_s_1.t) => not ((RSL.C_not RT_s_1.equ) (f1'1E24_, f2'1E8A_)) orelse (RT_s_1.equ (RT_s_1.R_inter (f1'1E24_, f2'1E8A_), RT_s_1.R_fromList []))) (fs'1DD5_)))) (fs'1DD5_))));
        
        fun isWellformed'1A35_ fs'1AA6_ = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (19, 11)); ((((reqNoEmptyFamilies'1BC5_) (fs'1AA6_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (19, 38)); ((reqNoDuplicateFamilyMembers'1D55_) (fs'1AA6_)))));
        
        fun reqNoFamilyMembersSeatedTogether'2269_ (p'22EE_, fs'22F1_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (40, 11)); ((RT_s_2.R_all (fn (t'2338_:RT_s_1.t) => ((RT_s_1.R_all (fn (p1'239E_:RT_Text.t) => ((RT_s_1.R_all (fn (p2'2404_:RT_Text.t) => not ((RSL.C_not RT_Text.equ) (p1'239E_, p2'2404_)) orelse (not (((areRelatives'1841_) (p1'239E_, p2'2404_, fs'22F1_))))) (t'2338_)))) (t'2338_)))) (p'22EE_))));
        
        fun reqEachFamilyMemberSeatedOnce'24C1_ (p'2543_, fs'2546_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (46, 13)); ((RT_s_2.R_all (fn (f'2592_:RT_s_1.t) => ((RT_s_1.R_all (fn (person'25FA_:RT_Text.t) => ((RT_s_2.R_exists1 (fn (t'2666_:RT_s_1.t) => RT_s_1.R_mem (person'25FA_, t'2666_)) (p'2543_)))) (f'2592_)))) (fs'2546_))));
        
        fun isCorrectPlan'1FAD_ (p'201F_, fs'2022_) = (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (33, 11)); ((((reqNoFamilyMembersSeatedTogether'2269_) (p'201F_, fs'2022_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (34, 12)); (((reqEachFamilyMemberSeatedOnce'24C1_) (p'201F_, fs'2022_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (35, 12)); (((reqNoEmptyTables'2719_) (p'201F_))) andalso (R_coverage.cancel(RT_Text.fromLit "./Basics.rsl", (36, 12)); ((reqAllFamilyMembersAreSeated'28A9_) (p'201F_, fs'2022_)))))));
        
        fun plan'2C1_ fs'32A_ = (R_coverage.cancel(RT_Text.fromLit "./Design.rsl", (8, 17)); if not(((isWellformed'1A35_) (fs'32A_))) then raise RSL.RSL_exception ("./Design.rsl:9:9: Precondition of plan" ^ "(" ^ RT_s_2.toString fs'32A_ ^ ")" ^ " not satisfied") else fs'32A_);
        
    end;
    
open Design;

RSL.print_load_errs();
RSL.set_time();
R_coverage.init();
(R_coverage.mark(RT_Text.fromLit "./Design.rsl", (8, 17), (49, 3));
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
RSL.print_error_count();
R_coverage.save_marked();
