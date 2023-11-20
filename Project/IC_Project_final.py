from manim import *
from manim import VGroup
import numpy as np

def example():
    Example = Text("Example : N = 2, K = 2",
                   font = "Consolas", font_size = 30,
                   t2c = {"Example" : GREY, "N" : GREEN, "K" : GREEN})
    Length_of_each_msg = MarkupText('<span fgcolor = "grey">L</span> = N<sup>K</sup> = 4 bits per message', 
                                    font = "Consolas", font_size = 30).shift(2*UP)

    return Example, Length_of_each_msg

def Msgs():
    W1 = Matrix([["a_2", "a_4", "a_1", "a_3"]],
                left_bracket = "\\langle",
                right_bracket = "\\rangle")
    W2 = Matrix([["b_1", "b_2", "b_3", "b_4"]],
                left_bracket = "\\langle",
                right_bracket = "\\rangle")
    
    return W1, W2

def Msg_in_Dbs():
    W_1 = Matrix([["a_2", "a_4", "a_1", "a_3"]])
    W_2 = Matrix([["b_2", "b_3", "b_1", "b_4"]])

    return W_1, W_2

def Random_perm_of_Msgs():
    W_1 = Matrix([["a_1", "a_2", "a_3", "a_4"]])
    W_2 = Matrix([["b_1", "b_2", "b_3", "b_4"]])

    return W_1, W_2

def Dbs():
    Db1 = Matrix([["a_2", "a_4", "a_1", "a_3"],
                  ["b_2", "b_3", "b_1", "b_4"]])
    Db2 = Matrix([["a_2", "a_4", "a_1", "a_3"],
                  ["b_2", "b_3", "b_1", "b_4"]])
    
    return Db1, Db2

def shift_by(VGroup, up, down, left, right):
    return VGroup.shift(up*UP + down*DOWN + left*LEFT + right*RIGHT)

def box_elems(List, color_to_fill, borders, h, w, Mobject, low_r, up_r):
    group = VGroup(*[Mobject(stroke_color = borders,
                    height = h,
                    width = w,).set_fill(color_to_fill, opacity = 0.5).move_to(List[e]) 
                    for e in range(low_r-1, up_r, 1)])
    
    return group

def create_queries(List_q, List_a, col_q, col_a, Mobject, h, w, low_r_q, up_r_q, low_r_a, up_r_a):
    box_q = box_elems(List_q, col_q, WHITE, h, w, Mobject, low_r_q, up_r_q)
    box_a = box_elems(List_a, col_a, WHITE, h, w, Mobject, low_r_a, up_r_a)
    # arrow_q_a = Arrow(start = start_arr, end = end_arr, color = col_arr)

    return box_q, box_a
# arrow_q_a

class Example(Scene):
    def construct(self):
        eg, L = example()
        g = VGroup(eg, L).arrange(DOWN)
        W_1, W_2 = Msgs()
        self.play(Write(eg), Write(L))
        self.wait()
        G = VGroup(W_1, W_2).arrange(DOWN)

        self.play(ReplacementTransform(g, G))
        self.wait()
        self.play(FadeOut(G))

####### Databases #######
        W1, W2 = Msgs()
        
        W_1, W_2 = Msg_in_Dbs()

        MsgG = Group(W1, W2).arrange_in_grid(row_alignments = "ud")
        MsgG_ = Group(W_1, W_2).arrange_in_grid(row_alignments = "ud")
        self.play(Transform(MsgG, MsgG_))
        self.wait()
        
        Db1, Db2 = Dbs()
        
        self.play(ReplacementTransform((Group(W1, W2)), Db1))
        self.wait()
        self.remove(Group(W1, W2))
        self.wait()
        self.play(FadeOut(Db1))
        # self.wait()

####### Desired Msgs #######
        Db1, Db2 = Dbs()
        W_1, W_2 = Random_perm_of_Msgs()
        self.play(Db1.animate.shift(3*LEFT + 2*DOWN), Db2.animate.shift(3*RIGHT + 2*DOWN))
        self.wait()
        Db1.set_row_colors(BLUE)
        Db2.set_row_colors(BLUE)
        self.wait()

        rows1 = Db1.get_rows()
        rows2 = Db2.get_rows()
        row1 = rows1[0].copy()
        row2 = rows2[0].copy()
        Db1.set_row_colors(WHITE)
        Db2.set_row_colors(WHITE)
        self.play(row1.animate.shift(2*UP + 3*RIGHT), row2.animate.shift(2*UP + 3*LEFT))
        self.wait()
        
        self.play(ReplacementTransform(Group(row1, row2), W_1))
        self.wait()

        text = Text("The desired message :",
                    font = "Consolas", font_size = 30,
                    t2c = {"The desired message" : BLUE}).shift(UP)
        self.play(FadeIn(text, shift = DOWN))
        self.wait()

        self.play(FadeOut(text, shift = UP),
                  FadeOut(W_1),
                  FadeOut(Db1, shift = LEFT),
                  FadeOut(Db2, shift = RIGHT))
        self.wait()

####### Extraction of bits #######
        Db1, Db2 = Dbs()
        W_1, W_2 = Random_perm_of_Msgs()

        db_name1 = Text("DB1",
                       font = "Consolas", font_size = 22,
                       t2c = {"DB1" : YELLOW})
        db_name2 = Text("DB2",
                       font = "Consolas", font_size = 22,
                       t2c = {"DB2" : YELLOW})

        db_grp1 = VGroup(Db1, db_name1).arrange(DOWN, buff = 0.3)
        db_grp2 = VGroup(Db2, db_name2).arrange(DOWN, buff = 0.3)
        db_grp1 = shift_by(db_grp1, 0, 2.5, 3, 0)
        db_grp2 = shift_by(db_grp2, 0, 2.5, 0, 3)
        group_of_Dbs = Group(db_grp1, db_grp2)
        self.add(group_of_Dbs)
        self.wait()

        Random_msg = Text("Take some random permutation of Msg1 and Msg2",
                          font = "Consolas", font_size = 30,
                          t2c = {"random" : BLUE, "Msg1" : GREEN, "Msg2" : RED})
        self.play(Write(Random_msg))

        arrow1 = Arrow(start = 0.5*UP + 0.6*LEFT, end = 3*LEFT + 2.5*UP, color = GREEN)
        arrow2 = Arrow(start = 0.6*RIGHT + 0.5*UP, end = 3*RIGHT + 2.5*UP, color = RED)
        self.play(Write(arrow1), Write(arrow2)) 
        W_1.shift(3*LEFT + 3*UP)
        W_2.shift(3*RIGHT + 3*UP)
        group_Random_perms = Group(W_1, W_2)
        
        self.play(FadeIn(group_Random_perms, shift = UP))
        self.wait()

        self.play(FadeOut(arrow1, arrow2))
        self.play(FadeOut(Random_msg, shift = DOWN))

        msg_rows_from_Dbs1 = Db1.get_rows()
        msg_rows_from_Dbs2 = Db2.get_rows()

        Queries_from_W_1 = W_1.get_rows()[0]
        Queries_from_W_2 = W_2.get_rows()[0]

        #Database symmetry
        dbSym = Text("DataBase Symmetry", font = "Consolas", font_size = 30,
                     t2c = {"DataBase Symmetry" : GREY}).shift(0.5*UP)
        self.play(Write(dbSym))
        self.wait()
        box_q1, box_a1= create_queries(Queries_from_W_1, msg_rows_from_Dbs1[0],
                                                     GREEN, PURPLE,
                                                     Rectangle, 0.5, 0.5,
                                                     1, 1, 3, 3)
        arrow_q1 = Arrow(start = 3*LEFT + 2.5*UP, end = 1.2*LEFT + 1*UP, color = GREEN)
        arrow_a1 = Arrow(start = 3*LEFT + 1*DOWN, end = 1.2*LEFT + 0*DOWN, color = GREEN)
        text = Text(" = a1",
                    font = "Consolas", font_size = 24).shift(0.5*DOWN)
        self.play(Create(box_q1))
        self.wait()
        self.play(Write(arrow_q1))
        self.wait()
        self.play(Create(box_a1))
        self.wait()
        self.play(Write(arrow_a1))
        self.wait()

        self.play(Write(text))
        self.play(FadeOut(text), FadeOut(arrow_q1), FadeOut(arrow_a1))
        self.wait()
        
        box_q2, box_a2= create_queries(Queries_from_W_1, msg_rows_from_Dbs2[0],
                                                     GREEN, ORANGE,
                                                     Rectangle, 0.5, 0.5,
                                                     2, 2, 1, 1)
        arrow_q2 = Arrow(start = 3*LEFT + 2.5*UP, end = 1.2*LEFT + 1*UP, color = GREEN)
        arrow_a2 = Arrow(start = 3*RIGHT + 1*DOWN, end = 1.2*RIGHT + 0*DOWN, color = RED)
        text = Text(" = a2",
                    font = "Consolas", font_size = 24).shift(0.5*DOWN)
        
        self.play(Create(box_q2))
        self.wait()
        self.play(Write(arrow_q2))
        self.wait()
        self.play(Create(box_a2))
        self.wait()
        self.play(Write(arrow_a2))
        
        self.play(Write(text))
        self.play(FadeOut(text), FadeOut(arrow_q2), FadeOut(arrow_a2))
        self.wait()
        self.play(FadeOut(dbSym))
        self.wait()

        # #Message Symmetry
        MsgSym = Text("Message Symmetry", font = "Consolas", font_size = 30,
                     t2c = {"Message Symmetry" : GREY}).shift(0.5*UP)
        self.play(Write(MsgSym))
        self.wait()
        box_q3, box_a3= create_queries(Queries_from_W_2, msg_rows_from_Dbs1[1],
                                                     RED, PURPLE,
                                                     Rectangle, 0.5, 0.5,
                                                     1, 1, 3, 3)
        arrow_q3 = Arrow(start = 3*RIGHT + 2.5*UP, end = 1.2*RIGHT + 1*UP, color = RED)
        arrow_a3 = Arrow(start = 3*LEFT + 1*DOWN, end = 1.2*LEFT + 0*DOWN, color = GREEN)
        text = Text(" = b1",
                    font = "Consolas", font_size = 24).shift(0.5*DOWN)
        
        self.play(Create(box_q3))
        self.wait()
        self.play(Write(arrow_q3))
        self.wait()
        self.play(Create(box_a3))
        self.wait()
        self.play(Write(arrow_a3))
        
        self.play(Write(text))
        self.play(FadeOut(text), FadeOut(arrow_q3), FadeOut(arrow_a3))
        self.wait()

        box_q4, box_a4= create_queries(Queries_from_W_2, msg_rows_from_Dbs2[1],
                                                     RED, RED,
                                                     Rectangle, 0.5, 0.5,
                                                     2, 2, 1, 1)
        arrow_q4 = Arrow(start = 3*RIGHT + 2.5*UP, end = 1.2*RIGHT + 1*UP, color = RED)
        arrow_a4 = Arrow(start = 3*RIGHT + 1*DOWN, end = 1.2*RIGHT + 0*DOWN, color = RED)
        text = Text(" = b2",
                    font = "Consolas", font_size = 24).shift(0.5*DOWN)
        
        self.play(Create(box_q4))
        self.wait()
        self.play(Write(arrow_q4))
        self.wait()
        self.play(Create(box_a4))
        self.wait()
        self.play(Write(arrow_a4))
        
        self.play(Write(text))
        self.play(FadeOut(text), FadeOut(arrow_q4), FadeOut(arrow_a4))
        self.wait()
        self.play(FadeOut(MsgSym))
        self.wait()

        #Exploit side queries
        ExpSide = Text("Exploiting Side Information", font = "Consolas", font_size = 30,
                     t2c = {"Exploiting Side Information" : GREY}).shift(0.5*UP)
        self.play(Write(ExpSide))
        self.wait()
        circle_q5 = Circle().surround(Queries_from_W_2[1], buffer_factor = 1.7)
        box_a5 = box_elems(msg_rows_from_Dbs1[0], PURPLE, WHITE, 0.5, 0.5, Rectangle, 4, 4)

        arrow_q5 = Arrow(start = 3*RIGHT + 2.5*UP, end = 1.2*RIGHT + 1*UP, color = RED)
        arrow_a5 = Arrow(start = 3*LEFT + 1*DOWN, end = 1.2*LEFT + 0*DOWN, color = GREEN)

        text = Text(" = b2 + a3", font = "Consolas",
                       font_size = 24).shift(0.5*DOWN)
        self.play(Create(circle_q5))
        self.wait()
        self.play(Write(arrow_q5))
        self.wait()
        self.play(Create(box_a5))
        self.wait()
        self.play(Write(arrow_a5))
        self.wait()

        self.play(Write(text))
        self.play(FadeOut(text), FadeOut(arrow_q5), FadeOut(arrow_a5))
        self.wait()

        circle_q6 = Circle().surround(Queries_from_W_2[0], buffer_factor = 1.7)
        box_a6 = box_elems(msg_rows_from_Dbs2[0], ORANGE, WHITE, 0.5, 0.5, Rectangle, 2, 2)
        
        arrow_q6 = Arrow(start = 3*RIGHT + 2.5*UP, end = 1.2*RIGHT + 1*UP, color = RED)
        arrow_a6 = Arrow(start = 3*RIGHT + 1*DOWN, end = 1.2*RIGHT + 0*DOWN, color = RED)

        text = Text(" = b1 + a4", font = "Consolas",
                       font_size = 24).shift(0.5*DOWN)
        self.play(Create(circle_q6))
        self.wait()
        self.play(Write(arrow_q6))
        self.wait()
        self.play(Create(box_a6))
        self.wait()
        self.play(Write(arrow_a6))
        self.wait()

        self.play(Write(text))
        self.play(FadeOut(text), FadeOut(arrow_q6), FadeOut(arrow_a6))
        self.wait()
        self.play(FadeOut(ExpSide))
        self.wait()
        
        self.play(FadeOut(box_q1), FadeOut(box_a1),
        FadeOut(box_q2), FadeOut(box_a2),
        FadeOut(box_q3), FadeOut(box_a3),
        FadeOut(box_q4), FadeOut(box_a4),
        FadeOut(circle_q5), FadeOut(box_a5),
        FadeOut(circle_q6), FadeOut(box_a6),
        FadeOut(W_1), FadeOut(W_2),
        FadeOut(db_grp1), FadeOut(db_grp2))
        self.wait()

####### Msg Reconstruction ########
        W_1, W_2 = Msg_in_Dbs()

        text = MarkupText("Finally, the extracted bits are - \n "
        '<span fgcolor = "orange"> a<sub>1</sub> </span>, <span fgcolor = "orange"> a<sub>2</sub> </span>, '
        '<span fgcolor = "green"> b<sub>1</sub> </span>, <span fgcolor = "green"> b<sub>2</sub> </span>, '
        '<span fgcolor = "green"> b<sub>2</sub> </span> + <span fgcolor = "orange"> a<sub>3</sub> </span> '
        '<span fgcolor = "green"> b<sub>1</sub> </span> + <span fgcolor = "orange"> a<sub>4</sub> </span>',
        font = "Consolas", font_size = 30
        )
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))

        '''speak here "since we know that a3 has been extracted after XORing with b2, we XOR it again with b2 to obtain the actual a3"
           and same goes for b1+a4'''
        
        b1 = MarkupText("a<sub>1</sub>", font = "Consolas", font_size = 30)
        b2 = MarkupText("a<sub>2</sub>", font = "Consolas", font_size = 30)
        b3 = MarkupText("b<sub>2</sub> + a<sub>3</sub> + b<sub>2</sub>",
                        font = "Consolas", font_size = 30)
        b4 = MarkupText("b<sub>1</sub> + a<sub>4</sub> + b<sub>1</sub>",
                        font = "Consolas", font_size = 30)
        arrow1 = Arrow(color = GOLD)
        arrow2 = Arrow(color = GOLD)
        arrow3 = Arrow(color = GOLD)
        arrow4 = Arrow(color = GOLD)

        ansB1 = MarkupText("a<sub>1</sub>", font = "Consolas", font_size = 30)
        ansB2 = MarkupText("a<sub>2</sub>", font = "Consolas", font_size = 30)
        ansB3 = MarkupText("a<sub>3</sub>",
                           font = "Consolas", font_size = 30)
        ansB4 = MarkupText("a<sub>4</sub>",
                           font = "Consolas", font_size = 30)

        g1 = VGroup(b1, arrow1, ansB1).arrange(RIGHT)
        g2 = VGroup(b2, arrow2, ansB2).arrange(RIGHT)
        g3 = VGroup(b3, arrow3, ansB3).arrange(RIGHT)
        g4 = VGroup(b4, arrow4, ansB4).arrange(RIGHT)
 
        g = VGroup(g1, g2, g3, g4).arrange(DOWN)
        self.play(Create(g1))
        self.wait()
        self.play(Create(g2))
        self.wait()
        self.play(Create(g3))
        self.wait()
        self.play(Create(g4))
        self.wait()

        self.play(FadeOut(g1), FadeOut(g2), FadeOut(g3), FadeOut(g4))
        self.wait()
        return 

class capacities(Scene):
    def construct(self):
        text1 = MathTex("Co = C_{\\epsilon}=(1+\\frac{1}{N}+\\frac{1}{N^2}+...+\\frac{1}{N^{K-1}})^{-1}")
        text3 = MathTex("=1+\\frac{1}{N}+\\frac{1}{N^2}+...+\\frac{1}{N^{K-1}})^{-1}")

        text2 = MathTex("C=(1+\\frac{1}{N}+\\frac{1}{N^2}+...+\\frac{1}{N^{K-1}})^{-1}")
        self.play(Write(text1))
        self.wait(8)
        self.play(ReplacementTransform(text1, text2))
        self.wait(5)
        self.play(FadeOut(text2))
        # self.wait()

class Non_colluding_Databases(Scene):
    def construct(self):

        #Images
        image1 = ImageMobject("database.png")
        image2 = ImageMobject("database.png")
        image3 = ImageMobject("database.png")
        image4 = ImageMobject("database.png")
        image5 = ImageMobject("database.png")
        image1.scale(0.15)
        image2.scale(0.15)
        image3.scale(0.15)
        image4.scale(0.15)
        image5.scale(0.15)
        target_position1 = np.array([0, 3.2, 0])
        target_position2 = np.array([-3.7, 1, 0])
        target_position3 = np.array([-2.3, -2.7, 0])
        target_position4 = np.array([2.3, -2.7, 0])
        target_position5 = np.array([3.7, 1, 0])
        image1.move_to(target_position1)
        image2.move_to(target_position2)
        image3.move_to(target_position3)
        image4.move_to(target_position4)
        image5.move_to(target_position5)

        self.play(FadeIn(image1, image2, image3, image4, image5), run_time=1.5)
        self.wait(1)

        arrow1 = DoubleArrow(start=UP, end=DOWN, color=WHITE, buff=0)
        cross1_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross1_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross1 = VGroup(cross1_h1, cross1_h2)
        arrow_with_cross1 = VGroup(arrow1, cross1)
        arrow_with_cross1.next_to(image1, RIGHT)
        arrow_with_cross1.rotate(PI/3)
        arrow_with_cross1.shift(RIGHT + DOWN*0.8)

        arrow2 = DoubleArrow(start=RIGHT, end=LEFT, color=WHITE, buff=0)
        cross2_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross2_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross2 = VGroup(cross2_h1, cross2_h2)
        arrow_with_cross2 = VGroup(arrow2, cross2)
        arrow_with_cross2.next_to(image2, UP) 
        arrow_with_cross2.rotate(PI/6)
        arrow_with_cross2.shift(RIGHT*1.6 + UP*0.35)

        arrow3 = DoubleArrow(start=RIGHT, end=LEFT, color=WHITE, buff=0)
        cross3_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross3_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross3 = VGroup(cross3_h1, cross3_h2)
        arrow_with_cross3 = VGroup(arrow3, cross3)
        target_position6 = np.array([0, -2.7, 0])
        arrow_with_cross3.move_to(target_position6)

        arrow4 = DoubleArrow(start=RIGHT, end=LEFT, color=WHITE, buff=0)
        cross4_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross4_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross4 = VGroup(cross4_h1, cross4_h2)
        arrow_with_cross4 = VGroup(arrow4, cross4)
        target_position7 = np.array([-3, -0.78, 0])
        arrow_with_cross4.rotate(-PI/(2.8))
        arrow_with_cross4.move_to(target_position7)


        arrow5 = DoubleArrow(start=RIGHT, end=LEFT, color=WHITE, buff=0)
        cross5_h1 = Line(start=UP*0.2 + RIGHT * 0.2, end=DOWN *
                        0.2 + LEFT * 0.2, color=RED, stroke_width=3)
        cross5_h2 = Line(start=UP*0.2 + LEFT * 0.2, end=DOWN *
                        0.2 + RIGHT * 0.2, color=RED, stroke_width=3)
        cross5 = VGroup(cross5_h1, cross5_h2)
        arrow_with_cross5 = VGroup(arrow5, cross5)
        target_position8 = np.array([3, -0.78, 0])
        arrow_with_cross5.rotate(PI/(2.8))
        arrow_with_cross5.move_to(target_position8)

        center_text1=Text("Non-Colluding")
        center_text1.shift(UP*0.4)
        center_text2=Text("Servers")
        center_text2.next_to(center_text1, DOWN*0.5)
        self.add(arrow_with_cross1, arrow_with_cross2, arrow_with_cross3, arrow_with_cross4, arrow_with_cross5)
        # Animate the fade in and fade out
        self.play(FadeIn(arrow_with_cross2, arrow_with_cross3, arrow_with_cross1, arrow_with_cross4, arrow_with_cross5, center_text1,center_text2), run_time=1.75)
        self.wait(4)
        self.play(FadeOut(arrow_with_cross1, arrow_with_cross2, arrow_with_cross3, arrow_with_cross5, arrow_with_cross4, image1, image2, image3, image4, image5, center_text1, center_text2), run_time=1.75)