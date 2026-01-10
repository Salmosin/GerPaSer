import math
import numpy as np
from Class_Tochka import Dot


class Ring(Dot):
    def __init__(self, koordinata_x, koordinata_y, minor_radius, major_radius):
        super().__init__(koordinata_x, koordinata_y)

        self.minor = minor_radius
        self.major = major_radius
        self.middle= (minor_radius+major_radius)/2
        self.points = self._generate_points_(45)

    def _generate_points_(self, number_of_points_in_row):
        points = []
        # Зададдим три радиуса на которых будут расположены точки как список
        conturs = [self.minor, self.middle, self.major]
        angles = []
        current_point = 1
        while current_point <= number_of_points_in_row:
            angles.append(current_point* 2 *math.pi/number_of_points_in_row)
            current_point += 1
        # По очереди работаем с контурами на разных радиусах


        for current_contur in conturs:
            ryad_tochek = []
            current_radius = current_contur

            for angle in angles:
                koordinata_x = self.x + current_radius * math.cos(angle)
                koordinata_y = self.y + current_radius * math.sin(angle)
                ryad_tochek.append(Dot (koordinata_x,koordinata_y))

            points.append(ryad_tochek)

        return points
    def list(self):
        flat = []
        for contur in self.points:
            flat.extend(contur)
        return flat

    def vivod_lista(self):
        all_points = self.list()
        current = -1
        massiv_points = np.zeros((2,len(all_points)))
        for point in all_points:
            current += 1
            massiv_points[0,current] = point.x
            massiv_points[1,current] = point.y
        return  massiv_points
    def print_table (self):
        print('x   |   y')
        massiv_tochek = self.vivod_lista()
        dlina = len(self.list()) - 1
        tochka = -1
        while tochka < dlina:
            tochka+=1
            print(f'{massiv_tochek[0,tochka]:.3f}', f'{massiv_tochek[1,tochka]:.3f}')

