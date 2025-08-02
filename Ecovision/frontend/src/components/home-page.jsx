// HomePage.jsx
import { Component } from "react";
import NewsCard from "./news-card";
import FeaturedCarousel from "./featured-carousel";

class HomePage extends Component {
  getCardSize = (index, importance) => {
    if (index === 0 && importance === "high") return "large";
    if (index === 4 && importance === "high") return "wide";
    return "medium";
  };

  render() {
    const { newsData } = this.props;

    // لاگ برای بررسی مقدار و نوع newsData دریافتی
    console.log("HomePage received newsData PROP:", newsData);
    console.log("Is newsData PROP an array in HomePage?:", Array.isArray(newsData));

    // بررسی برای اطمینان از اینکه newsData یک آرایه است و خالی نیست
    if (!newsData || !Array.isArray(newsData)) {
      // اگر newsData هنوز آماده نیست یا آرایه نیست، می‌توانید یک پیام یا null برگردانید
      // یا یک حالت پایه برای FeaturedCarousel و news-grid در نظر بگیرید
      console.warn("HomePage: newsData is not a valid array or is null/undefined.", newsData);
      return (
        <div className="home-page">
          <div className="page-header">
            <h2>Today's Economic News</h2>
            {/* بخش تاریخ می‌تواند همچنان نمایش داده شود */}
            <p className="date">
              {new Date().toLocaleDateString("en-US", {
                weekday: "long",
                year: "numeric",
                month: "long",
                day: "numeric",
              })}
            </p>
          </div>
          {/* <p>Loading news or no news available...</p> */}
          {/* یا می‌توانید FeaturedCarousel و news-grid را با آرایه خالی صدا بزنید اگر کامپوننت‌هایتان آن را مدیریت می‌کنند */}
           <FeaturedCarousel newsData={[]} />
           <div className="news-grid">{/* No items to display */}</div>
        </div>
      );
    }

    // اگر newsData یک آرایه معتبر است
    const itemsForCarousel = newsData.slice(0, Math.min(newsData.length, 4));
    const itemsForGrid = newsData; // یا newsData.slice(4) اگر نمی‌خواهید همپوشانی داشته باشند

    return (
      <div className="home-page">
        <FeaturedCarousel newsData={itemsForCarousel} />

        <div className="page-header">
          <h2>Today's Economic News</h2>
          <p className="date">
            {new Date().toLocaleDateString("en-US", {
              weekday: "long",
              year: "numeric",
              month: "long",
              day: "numeric",
            })}
          </p>
        </div>

        {itemsForGrid.length > 0 ? (
          <div className="news-grid">
            {itemsForGrid.map((news, index) => (
              <NewsCard
                key={news.id || index} // بهتر است همیشه id یکتا داشته باشید
                news={news}
                size={this.getCardSize(index, news.importance)}
              />
            ))}
          </div>
        ) : (
          <p>No news articles to display in the grid.</p>
        )}
      </div>
    );
  }
}

export default HomePage;