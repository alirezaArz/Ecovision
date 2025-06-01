import { Component } from "react"

class HeroSection extends Component {
  render() {
    return (
      <section className="hero-section">
        <div className="hero-content">
          <div className="hero-placeholder">
            <div className="hero-slide active">
              <div className="slide-content">
                <h2>Breaking: Federal Reserve Signals Rate Changes</h2>
                <p>Market analysts predict significant shifts in monetary policy following today's announcement...</p>
              </div>
            </div>
            <div className="hero-indicators">
              <span className="indicator active"></span>
              <span className="indicator"></span>
              <span className="indicator"></span>
              <span className="indicator"></span>
              <span className="indicator"></span>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default HeroSection
