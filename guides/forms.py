from django import forms

class GuideFilterForm(forms.Form):
    track = forms.ChoiceField(label='Трек', choices=[
        ('spa', 'Spa Francorchamps'),
        ('kyalami', 'Kyalami'),
        ('suzuka', 'Suzuka'),
        ('bathust', 'Bathurst'),
        ('monza', 'Monza'),
        ('nb_gt', 'Nurburgring GT'),
        ('nord', 'Nordschleife'),
        ('silver', 'Silverstone')
    ])
    
    car_class = forms.ChoiceField(label='Класс авто', choices=[
        ('gt2', 'GT2'),
        ('gt3', 'GT3'),
        ('gt4', 'GT4'),
        ('gtc', 'GTC')
    ], widget=forms.RadioSelect)
    
    
    gt2_cars = forms.ChoiceField(label='GT2', choices=[
            ('r8_gt2','Audi R8 LMS GT2'), 
            ('ktm_gt2','KTM X-Bow GT2'), 
            ('maser_gt2','Maserati MC20 GT2'), 
            ('mb_gt2','Mercedes-AMG GT2'),
            ('911_gt2','Porsche 991 II GT2 RS CS Evo'),
            ('935_gt2','Porsche 935 GT2')
        ])
    
    gt3_cars = forms.ChoiceField(label='GT3', choices=[
            ('f_296_gt3','Ferrari 296 GT3 '), 
            ('p_911_gt3','Porsche 911 (992) GT3 R'), 
            ('lambhevo2_gt3','Lamborghini Huracàn EVO2'),
            ('mcl720_evo_gt3','McLaren 720S GT3 Evo'),
            ('amv_gt3','2019 Aston Martin Racing V8 Vantage GT3'),
            ('ar8_gt3','2019 Audi R8 LMS Evo)'),
            ('ar8evo2_gt3','2022 Audi R8 LMS Evo II'),
            ('ben_gt3','2018 Bentley Continental GT3'),
            ('m4_gt3','2022 BMW M4 GT3'),
            ('m6_gt3','2017 BMW M6 GT3'),
            ('f488_gt3','2020 Ferrari 488 GT3 Evo'),
            ('lh_gt3','2019 Lamborghini Huracán GT3 Evo'),
            ('mb_gt3','2020 Mercedes AMG GT3'),
            ('p_911_2_gt3','2019 Porsche 911 II GT3R'),
            ('nsx_gt3','2019 Honda NSX GT3 Evo'),
            ('rcf_gt3','2016 Lexus RC F GT3'),
            ('720s_gt3','2019 McLaren 720S GT3'),
            ('mb2015_gt3','2015 Mercedes AMG GT3'),
            ('gtr_gt3','2018 Nissan GT-R NISMO GT3'),
            ('amv2013_gt3','2013 Aston Martin Racing V12 Vantage GT3'),
            ('r82015_gt3','2015 Audi R8 LMS'),
            ('ben2015_gt3','2015 Bentley Continental GT3'),
            ('emil_gt3','2012 Emil Frey Jaguar G3'),
            ('lamb2015_gt3','2015 Lamborghini Huracán GT3'),
            ('650s_gt3','2015 McLaren 650S GT3'),
            ('gtr2015_gt3','2015 Nissan GT-R NISMO GT3'),
            ('911_2018_gt3','2018 Porsche 911 GT3 R'),
            ('reiter_gt3','2017 Reiter Engineering R-EX GT3')
        ])
    
    gt4_cars = forms.ChoiceField(label='GT4', choices=[
            ('alp_gt4','Alpine A110 2018'),
            ('amr_gt4','AMR V8 Vantage 2018'),
            ('r8_gt4','Audi R8 LMS 2018'),
            ('m4_gt4','BMW M4 2018'),
            ('camaro_gt4','Chevrolet Camaro R 2017'),
            ('ginetta_gt4','Ginetta G55 2012'),
            ('ktm_gt4','KTM X-Bow 2016 2016'),
            ('maser_gt4','Maserati Granturismo MC 2016'),
            ('570s_gt4','McLaren 570S 2016'),
            ('mb_gt4','Mercedes AMG 2016'),
            ('718_gt4','Porsche 718 Cayman GT4 Clubsport 2019')
        ])