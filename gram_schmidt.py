import math

#Turns a list of linearly independent vectors into an orthonormal basis
def gram_schmidt(vectors):
	orthoNormBasis = []

	for i in range(len(vectors)):
		u_i = vectors[i]

		for j in range(len(orthoNormBasis)):
			projection = proj(orthoNormBasis[j], u_i)

			for k in range(len(projection)):
				u_i[k] -= projection[k]

		u_i_norm = math.sqrt(dotProd(u_i, u_i))

		for j in range(len(u_i)):
			u_i[j] /= math.sqrt(u_i_norm)

		orthoNormBasis.append(u_i)

	return orthoNormBasis

#Returns the projection of vector v onto u
def proj(u, v):
	scale = dotProd(u, v)/dotProd(u, u)
	return [scale*u[i] for i in range(len(u))]

#Returns the dot product of vectors u and v
def dotProd(u, v):
	return sum(u[i]*v[i] for i in range(len(u)))
