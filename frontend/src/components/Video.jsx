import React from 'react'

function Video({
	// id,
	videoSource,
	videoHeader,
	// videoTitle,
	// videoLikes,
	// videoDisLikes,
	videoViews,
	videoAuthor
	// authorAvatar
}) {
	return (
		<div className="video">
			<div className="thumbnail">
				<video>{videoSource}</video>
			</div>

			<div className="details">
				<div className="author">
					<img
						src={
							'https://www.freecodecamp.org/news/content/images/2022/01/yt-logo.png'
						}
						alt="authorAvatar"
					/>
				</div>
				<div className="title">
					<h3>{videoHeader}</h3>
					<a href="">{videoAuthor}</a>
					<span>• {videoViews} •</span>
				</div>
			</div>
		</div>
	)
}

export default Video
