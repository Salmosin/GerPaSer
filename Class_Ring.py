import math
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
        return all_points
        #current = 0
        #for point in all_points:
        #    current += 1
        #    print(current, '|', f"{point.x:.3f}", "|", f"{point.y:.3f}")


