from manim import *

class KvadratickaFunkcia(Scene):
    def construct(self):
        uvodText = Text("Kvadratická Funkcia",
        t2c = {"Kvadratická": YELLOW, "Funkcia":RED})

        uvodVzorecKvadraticka = MathTex("{y = ax^2 + bx + c}", font_size=50).to_edge(UL).set_color(YELLOW)
        uvodVzorecKvadraticka[0][2].set_color(RED)
        uvodVzorecKvadraticka[0][6].set_color(RED)
        uvodVzorecKvadraticka[0][9].set_color(RED)
        boxVzorecKvadraticka = SurroundingRectangle(uvodVzorecKvadraticka, color=WHITE, buff=0.3)

        arrow1 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=10).next_to(uvodVzorecKvadraticka[0][2], DOWN)
        arrow2 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=10).next_to(uvodVzorecKvadraticka[0][6], DOWN)
        arrow3 = Arrow(start=ORIGIN, end=DOWN, color=WHITE, buff=10).next_to(uvodVzorecKvadraticka[0][9], DOWN)

        textPodmienky = MathTex("a,b,c \in R").next_to(arrow2, DOWN).shift(LEFT*0.5)              # to /in je v dokumentacií pre symboly pre LaTex
        textPodmienky[0][0].set_color(RED)
        textPodmienky[0][2].set_color(RED)  
        textPodmienky[0][4].set_color(RED) 
        multipleObjects= VGroup(uvodVzorecKvadraticka, boxVzorecKvadraticka, arrow1,arrow2,arrow3,textPodmienky) 

        textParabola = Text("Grafom funkcie je parabola", font_size=25,
        t2c= {"parabola":YELLOW}).to_edge(UL)

        suradnicovaOs = Axes(                                                                
            x_range=[-8,8,1],
            y_range=[-8,8,1],
            tips=False,
            x_length=10,
            y_length=10,
           
            axis_config=
            {
            "stroke_color": GREY_A,
            "include_numbers": True,
            }
        )
        parabola = suradnicovaOs.plot(lambda y: 0.5 * y ** 2 - 0.5, x_range=[-4,4])

        self.play(Write(uvodText), run_time=2)
        self.play(Unwrite(uvodText))
        self.play(Write(suradnicovaOs), run_time=3)
        self.play(Write(uvodVzorecKvadraticka))
        self.play(Create(boxVzorecKvadraticka))
        self.play(FadeIn(arrow1,arrow2,arrow3))
        self.play(Write(textPodmienky))
        self.wait()

        self.play(Unwrite(multipleObjects))
        self.play(Write(textParabola))
        self.play(Write(parabola))
        self.wait()
  




        