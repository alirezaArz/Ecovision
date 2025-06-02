import { Component } from "react";
import Header from "./components/header";
import Sidebar from "./components/sidebar";
import HomePage from "./components/home-page";
import "./styles.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchQuery: "",
      selectedCategory: "all",
      newsData: [
        // ... (داده‌های اخبار شما بدون تغییر باقی می‌مانند)
        {
          id: 1,
          title: "Federal Reserve Signals Potential Rate Cut in 2025",
          summary:
            "The Federal Reserve indicated a possible shift in monetary policy as inflation shows signs of cooling, suggesting potential rate cuts in the coming year.",
          image: "/placeholder.svg?height=200&width=300",
          category: "Monetary Policy",
          importance: "high",
          date: "2025-01-31",
        },
        {
          id: 2,
          title: "Tech Stocks Rally on Strong Earnings Reports",
          summary: "Major technology companies exceeded quarterly expectations, driving market optimism.",
          image: "/placeholder.svg?height=150&width=250",
          category: "Markets",
          importance: "medium",
          date: "2025-01-31",
        },
        {
          id: 3,
          title: "Global Supply Chain Disruptions Ease",
          summary: "International shipping costs decline as port congestion clears and supply chains normalize.",
          image: "/placeholder.svg?height=180&width=280",
          category: "Trade",
          importance: "medium",
          date: "2025-01-31",
        },
        {
          id: 4,
          title: "Unemployment Rate Hits Historic Low",
          summary:
            "The national unemployment rate dropped to 3.2%, marking the lowest level in decades as job creation continues.",
          image: "/placeholder.svg?height=220&width=320",
          category: "Employment",
          importance: "high",
          date: "2025-01-31",
        },
        {
          id: 5,
          title: "Oil Prices Stabilize Amid OPEC Agreement",
          summary: "Crude oil prices find equilibrium following new production agreements.",
          image: "/placeholder.svg?height=160&width=240",
          category: "Energy",
          importance: "low",
          date: "2025-01-31",
        },
        {
          id: 6,
          title: "Housing Market Shows Signs of Recovery",
          summary: "Home sales increase for third consecutive month as mortgage rates decline.",
          image: "/placeholder.svg?height=190&width=290",
          category: "Real Estate",
          importance: "medium",
          date: "2025-01-31",
        },
        {
          id: 7,
          title: "Cryptocurrency Regulation Framework Announced",
          summary: "Government unveils comprehensive guidelines for digital asset trading and taxation.",
          image: "/placeholder.svg?height=170&width=260",
          category: "Crypto",
          importance: "high",
          date: "2025-01-31",
        },
        {
          id: 8,
          title: "Consumer Spending Exceeds Expectations",
          summary: "Retail sales surge 5.2% month-over-month, signaling strong consumer confidence.",
          image: "/placeholder.svg?height=200&width=300",
          category: "Consumer",
          importance: "medium",
          date: "2025-01-31",
        },
      ],
      cryptoData: [], // مقدار اولیه را خالی یا null بگذارید
      theme: "dark", // مقدار theme را می‌توانید همچنان از اینجا یا از API بگیرید
    };
  }

  componentDidMount() {
    // درخواست برای دریافت داده‌های cryptoData
    fetch("http://127.0.0.1:8000/crypto-data/") // آدرس API جنگو
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        this.setState({ cryptoData: data });
        // اگر theme را هم از API می‌گیرید:
        // this.setState({ cryptoData: data.cryptoData, theme: data.theme });
      })
      .catch((error) => {
        console.error("There has been a problem with your fetch operation:", error);
      });
  }

  handleSearch = (query) => {
    this.setState({ searchQuery: query });
  };

  handleCategorySelect = (category) => {
    this.setState({ selectedCategory: category });
  };

  getFilteredNews = () => {
    const { newsData, searchQuery, selectedCategory } = this.state;
    let filtered = newsData;

    if (selectedCategory !== "all") {
      filtered = filtered.filter((news) => news.category.toLowerCase() === selectedCategory.toLowerCase());
    }

    if (searchQuery) {
      filtered = filtered.filter(
        (news) =>
          news.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
          news.summary.toLowerCase().includes(searchQuery.toLowerCase()) ||
          news.category.toLowerCase().includes(searchQuery.toLowerCase())
      );
    }

    return filtered;
  };

  render() {
    const { theme } = this.state;
    // نمایش یک پیام "در حال بارگذاری" تا زمانی که داده‌ها دریافت شوند
    if (this.state.cryptoData.length === 0) {
        return <div>Loading crypto data...</div>;
    }

    return (
      <div className={`app ${theme}`}>
        <Header onSearch={this.handleSearch} />
        <div className="app-body">
          <Sidebar
            onCategorySelect={this.handleCategorySelect}
            onSearch={this.handleSearch}
            cryptoData={this.state.cryptoData} // استفاده از داده‌های دریافت شده
          />
          <main className="main-content">
            <HomePage newsData={this.getFilteredNews()} />
          </main>
        </div>
      </div>
    );
  }
}

export default App;