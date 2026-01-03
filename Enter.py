import matplotlib.pyplot as plt
import math

class Dot(object):
    def __init__(self, koordinata_x, koordinata_y):
        self.x = koordinata_x
        self.y = koordinata_y

    def __str__(self):
        return self.x, self.y

    def print(self):
        print(self.__str__())

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
        current = 0
        for point in all_points:
            current += 1
            print(current, '|', f"{point.x:.3f}", "|", f"{point.y:.3f}")

    def risunok(self):
        tochki = self.list()
        plt.figure(figsize=(self.major, self.major))

        koordinati_x = [tochka.x for tochka in tochki]
        koordinati_y = [tochka.y for tochka in tochki]
        plt.scatter(koordinati_x,koordinati_y,s=100, c='green', alpha=0.7, edgecolors='black')
        plt.show()
lol = Dot(1,1)
lol.print()

Rum = Ring(230,125, 4, 6)
Rum.vivod_lista()
Rum.risunok()

