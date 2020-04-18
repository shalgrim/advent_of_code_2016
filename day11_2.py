from day11_1 import RG, RM, CoG, CoM, CuG, CuM, PlG, PlM, PrG, PrM, shortest_path_solver

DG = 'DG'
DM = 'DM'
EG = 'EG'
EM = 'EM'

FLOORS2 = [
    [PrG, PrM, DG, DM, EG, EM],
    [CoG, CuG, RG, PlG],
    [CoM, CuM, RM, PlM],
    [],
]
if __name__ == '__main__':
    print(shortest_path_solver(FLOORS2))
