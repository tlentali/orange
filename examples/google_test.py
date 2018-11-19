from __future__ import print_function

from ortools.linear_solver import pywraplp


def main():
    # Create the linear solver with the GLOP backend.
    solver = pywraplp.Solver(
        'simple_lp_program',
        pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # Create the variables x and y.
    x = solver.NumVar(0, 1, 'x')
    y = solver.NumVar(0, 2, 'y')

    # Create a linear constraint, 0 <= x + y <= 2.
    ct = solver.Constraint(0, 2, 'ct')
    ct.SetCoefficient(x, 1)
    ct.SetCoefficient(y, 1)

    # Create the objective function, 3 * x + y.
    objective = solver.Objective()
    objective.SetCoefficient(x, 3)
    objective.SetCoefficient(y, 1)
    objective.SetMaximization()

    # Call the solver and display the results.
    solver.Solve()
    print('Solution:')
    print('Objective value = ', objective.Value())
    print('x = ', x.solution_value())
    print('y = ', y.solution_value())


if __name__ == '__main__':
    main()
