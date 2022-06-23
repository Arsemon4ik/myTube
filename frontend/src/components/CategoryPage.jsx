import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import axios from 'axios'
import { Table } from 'react-bootstrap'

function CategoryPage() {
	const [categoryRecipes, setCategoryRecipes] = useState([])
	const [categoryData, setCategoryData] = useState({})
	const params = useParams()
	const categoryId = parseFloat(params.id)

	const getCategory = () => {
		axios(`http://127.0.0.1:8000/categories/${categoryId}/`).then(
			(response) => setCategoryData(response.data)
		)
	}
	const getRecipes = () => {
		axios(`http://localhost:8000/recipes/`).then((response) => {
			const data = response.data
			const data_filtered = data.filter(
				(item) => item.categoryId === categoryId
			)
			setCategoryRecipes(data_filtered)
		})
	}

	// }
	useEffect(() => {
		getCategory()
		getRecipes()
	}, [])

	return (
		<>
			<h1>{categoryData.categoryName}</h1>
			<Table>
				<thead>
					<tr>
						<th>Рецепты</th>
					</tr>
				</thead>
				<tbody>
					{categoryRecipes.map((recipe) => (
						<tr key={recipe.recipeName}>
							<td>
								<a href={`/recipes/${recipe.id}`}>
									{recipe.recipeName}
								</a>
							</td>
							<td>{recipe.recipeText.slice(0, 100) + '...'}</td>
						</tr>
					))}
				</tbody>
			</Table>
		</>
	)
}

export default CategoryPage
