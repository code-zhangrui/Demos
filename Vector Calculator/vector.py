# -*- coding: UTF-8 -*-

from math import sqrt, acos, pi
from decimal import Decimal, getcontext

class Vector(object):
	CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
	NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'No unique orthogonal component'
	NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
	ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Cross function is only defined for 2d and 3d'

	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple([Decimal(x) for x in coordinates])
			self.dimension = len(self.coordinates)
			self.idx = 0

		except ValueError:
			raise ValueError('The coordinates must be nonempty')

		except TypeError:
			raise TypeError('The coordinates must be an iterable')

	def area_of_triangle_with(self, v):
		return self.area_of_parallelogram_with(v)/Decimal(2.0)

	def area_of_parallelogram_with(self, v):
		cross_product = self.cross(v)
		#取向量积的大小
		return cross_product.magnitude()

	def cross(self, v):
		try:
			x_1, y_1, z_1 = self.coordinates
			x_2, y_2, z_2 = v.coordinates
			new_coordinates = [ y_1*z_2 - y_2*z_1,
								x_2*z_1 - x_1*z_2,
								x_1*y_2 - x_2*y_1 ]
			return Vector(new_coordinates)

		except ValueError as e:
			msg = str(e)
			if msg == 'need more than 2 values to unpack':
				#如果向量是二维的，就向每个向量中添加为 0 的 z 轴坐标
				self_embedded_in_R3 = Vector(self.coordinates + ('0',))
				v_embedded_in_R3 = Vector(v.coordinates + ('0',))
				return self_embedded_in_R3.cross(v_embedded_in_R3)
			elif(msg == 'too many values to unpack' or
				 msg == 'need more than 1 value to unpack'):
				raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
			else:
				raise e

	#在基向量上的正交边
	def component_orthogonal_to(self, basis):
		try:
			projection = self.component_parallel_to(basis)
			return self.minus(projection)

		except Exception as e:
			if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
				raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
			else:
				raise e

	#在基向量上的平行边
	def component_parallel_to(self, basis):
		try:
			u = basis.normalized()
			weight = self.dot(u)
			return u.times_scalar(weight)

		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
			else:
				raise e

	#tolerance 是公差；abs() 返回一个绝对值；1e-10 是 1 乘以10的-10次方
	#正交性判断
	def is_orthogonal_to(self, v, tolerance=1e-10):
		return abs(self.dot(v)) < tolerance

	#平行性判断
	def is_parallel_to(self, v):
		return(self.is_zero() or v.is_zero() or self.angle_with(v) == 0 or self.angle_with(v) == pi)

	def is_zero(self, tolerance=1e-10):
		return self.magnitude() < tolerance

	#求点积
	def dot(self, v):
		return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

	def angle_with(self, v, in_degrees=False):
		try:
			u1 = self.normalized()
			u2 = v.normalized()
			angle_in_radians = acos(round(u1.dot(u2),2))

			if in_degrees:
				degrees_per_radian = 180./pi
				return angle_in_radians*degrees_per_radian
			else:
				return angle_in_radians

		except Exception as e:
			if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
				raise Exception('Cannot compute an angle with zero vector')
			else:
				raise e

	#向量长度
	def magnitude(self):
		return Decimal(sqrt(sum([x**2 for x in self.coordinates])))

	#标准化向量 u
	def normalized(self):
		try:
			magnitude = self.magnitude()
			return self.times_scalar(Decimal('1.0')/magnitude)

		except ZeroDivisionError:
			raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

	def plus(self, v):
		new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def minus(self, v):
		new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	#标量乘法
	def times_scalar(self, c):
		new_coordinates = [Decimal(c)*x for x in self.coordinates]
		return Vector(new_coordinates)

	#控制 print 的输出；format 括号中的内容置换到前面的 {} 里
	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	#比较向量是否相等
	def __eq__(self, v):
		return self.coordinates == v.coordinates

    # __iter__ 和 next 是一个迭代器
	def __iter__(self):
		return self

	def next(self):
		self.idx += 1
		try:
			return Decimal(self.coordinates[self.idx-1])
		except IndexError:
			self.idx = 0
			raise StopIteration  # Done iterating.

    # 将自己返回成 iterable 的形式
	def __getitem__(self,index):
		return Decimal(self.coordinates[index])

# v = Vector([1.5, 9.547, 3.691])
# w = Vector([-6.007, 0.124, 5.772])
# print(v.area_of_triangle_with(w))
