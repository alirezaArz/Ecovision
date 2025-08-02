"use client"

import { Component } from "react"

class FeaturedCarousel extends Component {
  constructor(props) {
    super(props)
    this.state = {
      currentSlide: 0,
      isAutoPlaying: true,
    }
    this.autoPlayInterval = null
  }

  componentDidMount() {
    this.startAutoPlay()
  }

  componentWillUnmount() {
    this.stopAutoPlay()
  }

  startAutoPlay = () => {
    if (this.state.isAutoPlaying) {
      this.autoPlayInterval = setInterval(() => {
        this.nextSlide()
      }, 5000) // Change slide every 5 seconds
    }
  }

  stopAutoPlay = () => {
    if (this.autoPlayInterval) {
      clearInterval(this.autoPlayInterval)
      this.autoPlayInterval = null
    }
  }

  nextSlide = () => {
    const { newsData } = this.props
    this.setState((prevState) => ({
      currentSlide: (prevState.currentSlide + 1) % newsData.length,
    }))
  }

  prevSlide = () => {
    const { newsData } = this.props
    this.setState((prevState) => ({
      currentSlide: prevState.currentSlide === 0 ? newsData.length - 1 : prevState.currentSlide - 1,
    }))
  }

  goToSlide = (index) => {
    this.setState({ currentSlide: index })
  }

  handleMouseEnter = () => {
    this.stopAutoPlay()
  }

  handleMouseLeave = () => {
    this.startAutoPlay()
  }

  render() {
    const { newsData } = this.props
    const { currentSlide } = this.state

    if (!newsData || newsData.length === 0) return null

    return (
      <div className="featured-carousel" onMouseEnter={this.handleMouseEnter} onMouseLeave={this.handleMouseLeave}>
        <div className="carousel-container">
          <div className="carousel-slides" style={{ transform: `translateX(-${currentSlide * 100}%)` }}>
            {newsData.map((news, index) => (
              <div key={news.id} className="carousel-slide">
                <div className="slide-image">
                  <img src={news.image || "/placeholder.svg?height=400&width=800"} alt={news.title} />
                  <div className="slide-overlay" />
                </div>
                <div className="slide-content">
                  <div className="slide-badge">{news.category}</div>
                  <h3 className="slide-title">{news.title}</h3>
                  <p className="slide-summary">{news.summary}</p>
                  <div className="slide-meta">
                    <span className="slide-date">
                      {new Date(news.date).toLocaleDateString("en-US", {
                        month: "long",
                        day: "numeric",
                        year: "numeric",
                      })}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Navigation Arrows */}
          <button className="carousel-nav carousel-nav-prev" onClick={this.prevSlide}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <polyline points="15,18 9,12 15,6"></polyline>
            </svg>
          </button>
          <button className="carousel-nav carousel-nav-next" onClick={this.nextSlide}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <polyline points="9,18 15,12 9,6"></polyline>
            </svg>
          </button>

          {/* Slide Indicators */}
          <div className="carousel-indicators">
            {newsData.map((_, index) => (
              <button
                key={index}
                className={`carousel-indicator ${index === currentSlide ? "active" : ""}`}
                onClick={() => this.goToSlide(index)}
              />
            ))}
          </div>
        </div>
      </div>
    )
  }
}

export default FeaturedCarousel
