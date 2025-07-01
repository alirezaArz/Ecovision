import { Component } from "react";
import Sidebar from "./components/sidebar";
import HomePage from "./components/home-page";
import "./styles.css";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      searchQuery: "",
      selectedCategory: "all",
      newsData: [],
      cryptoData: [],
      isLoading: true,
      error: null,
      theme: "dark",
    };
  }

  componentDidMount() {
    this.setState({ isLoading: true, error: null });
    Promise.all([
      fetch('http://127.0.0.1:8000/news/').then(res => {
        if (!res.ok) throw new Error(`News API Error: ${res.status} ${res.statusText}`);
        return res.json();
      }),
      fetch('http://127.0.0.1:8000/crypto/').then(res => {
        if (!res.ok) throw new Error(`Crypto API Error: ${res.status} ${res.statusText}`);
        return res.json();
      })
    ])
    .then(([newsDataResponse, cryptoDataResponse]) => {
      console.log("Raw newsDataResponse from API:", newsDataResponse);
      console.log("Raw cryptoDataResponse from API:", cryptoDataResponse);
      console.log("API newsData content IS ARRAY?:", Array.isArray(newsDataResponse.newsData));
      console.log("API newsData content LENGTH:", newsDataResponse.newsData ? newsDataResponse.newsData.length : 'N/A');

      this.setState({
        newsData: newsDataResponse.newsData || [],
        cryptoData: cryptoDataResponse.cryptoData || cryptoDataResponse || [],
        isLoading: false
      }, () => {
        console.log("App.js STATE AFTER fetch - this.state.newsData:", this.state.newsData);
        console.log("App.js STATE AFTER fetch - newsData LENGTH:", this.state.newsData.length);
        console.log("App.js STATE AFTER fetch - isLoading:", this.state.isLoading);
      });
    })
    .catch(error => {
      console.error("Error fetching data:", error);
      this.setState({ error: error.message, isLoading: false });
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

    if (!filtered || !Array.isArray(filtered) || filtered.length === 0) {
        return [];
    }

    if (selectedCategory && selectedCategory.toLowerCase() !== "all") {
      filtered = filtered.filter((news) => news.category && news.category.toLowerCase() === selectedCategory.toLowerCase());
    }

    if (searchQuery) {
      const lowercasedQuery = searchQuery.toLowerCase();
      filtered = filtered.filter(
        (news) =>
          (news.title && news.title.toLowerCase().includes(lowercasedQuery)) ||
          (news.summary && news.summary.toLowerCase().includes(lowercasedQuery)) ||
          (news.category && news.category.toLowerCase().includes(lowercasedQuery))
      );
    }
    return filtered;
  };

  render() {
    const { theme, cryptoData, isLoading, error, newsData, selectedCategory, searchQuery } = this.state;

    console.log("App.js RENDER - current state.newsData:", newsData);
    console.log("App.js RENDER - current state.newsData LENGTH:", newsData ? newsData.length : 'N/A - newsData is null/undefined');
    console.log("App.js RENDER - current state.selectedCategory:", selectedCategory);
    console.log("App.js RENDER - current state.searchQuery:", searchQuery);
    console.log("App.js RENDER - current state.isLoading:", isLoading);
    console.log("App.js RENDER - current state.error:", error);


    if (isLoading) {
      return <div className={`app ${theme}`}>در حال بارگذاری داده‌ها...</div>;
    }

    if (error) {
      return <div className={`app ${theme}`}>خطا: {error}. لطفاً صفحه را رفرش کنید.</div>;
    }

    const filteredNews = this.getFilteredNews();
    console.log("App.js RENDER - filteredNews RESULT:", filteredNews);
    console.log("App.js RENDER - filteredNews LENGTH:", filteredNews.length);


    return (
      <div className={`app ${theme}`}>
        <div className="app-body">
          <Sidebar
            onCategorySelect={this.handleCategorySelect}
            onSearch={this.handleSearch}
            cryptoData={cryptoData}
          />
          <main className="main-content">
            <HomePage newsData={filteredNews} />
          </main>
        </div>
      </div>
    );
  }
}

export default App;