from django.core.management.base import BaseCommand, CommandError
from shoes.models import Manufacturer, ShoeType, ShoeColor, Shoe

# Found this video really useful: https://www.youtube.com/watch?v=V0RfgNIwCqI&list=FLr_YmgbEiSBH9wuGz-Fjl2A&index=1&ab_channel=PrettyPrinted # noqa
# Thanks to Alex Mourtos for helping me simplify my command dramatically. I originally made it more complicated than it needed to be.

class Command(BaseCommand):
    help = 'Fill up the ShoeType and ShoeColor Fields'

    def handle(self, *args, **options):
        types = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        for taipu in types:
            if ShoeType.objects.filter(style=taipu).exists():
                self.stdout.write(self.style.WARNING('Type already exists!'))
                continue
            taipu = ShoeType.objects.create(style=taipu)
            self.stdout.write(self.style.SUCCESS('ShoeType added!'))

        colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet', 'White', 'Black']
        for iro in colors:
            if ShoeColor.objects.filter(color_name=iro).exists():
                self.stdout.write(self.style.WARNING('Color already exists!'))
                continue
            iro = ShoeColor.objects.create(color_name=iro)
            self.stdout.write(self.style.SUCCESS('ShoeColor added!'))

    # def add_arguments(self, parser):
        # parser.add_argument('style', choices=['sneaker', 'boot', 'sandal', 'dress', 'other'], help='choose a style')        
        # parser.add_argument('style', nargs=5, default='sneaker', help='Pass in any 5 strings to populate the shoetypes')
        # parser.add_argument('color_name', nargs=9, default='Blue', help='Pass in any 9 strings to populate the shoe colors')

        # for num in options['style']:
        #     s_type = ShoeType(
        #         style='sneaker'
        #     )
        #     s_type2 = ShoeType(
        #         style='boot'
        #     )
        #     s_type3 = ShoeType(
        #         style='sandal'
        #     )
        #     s_type4 = ShoeType(
        #         style='dress'
        #     )
        #     s_type5 = ShoeType(
        #         style='other'
        #     )
        # s_type.save()
        # s_type2.save()
        # s_type3.save()
        # s_type4.save()
        # s_type5.save()
        # self.stdout.write(self.style.SUCCESS('ShoeType added!'))

        # for color in options['color_name']:
        #     s_color = ShoeColor(
        #         color_name='Red'
        #     )
        #     s_color2 = ShoeColor(
        #         color_name='Orange'
        #     )
        #     s_color3 = ShoeColor(
        #         color_name='Yellow'
        #     )
        #     s_color4 = ShoeColor(
        #         color_name='Green'
        #     )
        #     s_color5 = ShoeColor(
        #         color_name='Blue'
        #     )
        #     s_color6 = ShoeColor(
        #         color_name="Indigo"
        #     )
        #     s_color7 = ShoeColor(
        #         color_name="Violet"
        #     )
        #     s_color8 = ShoeColor(
        #         color_name='White'
        #     )
        #     s_color9 = ShoeColor(
        #         color_name='Black'
        #     )
        # s_color.save()
        # s_color2.save()
        # s_color3.save()
        # s_color4.save()
        # s_color5.save()
        # s_color6.save()
        # s_color7.save()
        # s_color8.save()
        # s_color9.save()
        # self.stdout.write(self.style.SUCCESS('ShoeColor added!'))
