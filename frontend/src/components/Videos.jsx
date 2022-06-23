import React, { useEffect, useState } from 'react'
import Video from './Video'

function Videos() {
	const [data, setData] = useState([])

	// const getVideos = () => {
	// 	axios
	// 		.get('http://localhost:8000/tube/videos/')
	// 		.then((response) => console.log(response.data))
	// 	// .then((response) => setData(response.data))
	// }
	const getVideos = async () => {
		await fetch('http://localhost:8000/tube/videos/', {
			method: 'GET'
		})
			.then((response) => response.json())
			.then((data) => setData(data))
	}
	useEffect(() => {
		getVideos()
		// console.log(data[0])
	}, [])
	return (
		<>
			{data.map((value) => (
				<Video
					id={value.id}
					valueSource={value.valueSource}
					valueHeader={value.valueHeader}
					valueTitle={value.valueTitle}
					valueViews={value.valueViews}
					key={value.id}
				/>
			))}
			{/*<h1>{data[0].id}</h1>*/}
		</>
	)
}

export default Videos
