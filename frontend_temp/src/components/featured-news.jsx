"use client"

import { Component } from "react"

class FeaturedNews extends Component {
  render() {
    const { featuredNewsIndex } = this.props

    return (
      <section className="featured-news">
        <div className="featured-content">
          <div className="featured-background">
            <div className="featured-overlay">
              <div className="featured-text">
                <h2 className="featured-title">Featured News</h2>
                <p className="featured-description">
                  Stay updated with the latest economic developments and market insights
                </p>
              </div>
            </div>
            {/* Carousel Indicators */}
            <div className="featured-indicators">
              {[0, 1, 2, 3].map((index) => (
                <div key={index} className={`indicator ${index === featuredNewsIndex ? "active" : ""}`} />
              ))}
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default FeaturedNews
