def square_matrix_simple(matrix=[]):
  """Returns a new matrix where each element is the square of the corresponding element in the original matrix."""

  new_matrix = []
  for row in matrix:
    new_row = []
    for element in row:
      new_row.append(element ** 2)
    new_matrix.append(new_row)

  return new_matrix
