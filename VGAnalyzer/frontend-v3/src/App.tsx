import { Search, Globe } from "lucide-react"
import { Button } from "./components/ui/button"
import { Input } from "./components/ui/input"

function App() {
  const popularSearches = [
    "Market Trends",
    "Investment Strategies",
    "Financial Analysis",
    "Economic Forecasts",
    "Global Economy",
  ]

  const newsCategories = [
    "Economy",
    "Finance",
    "Markets",
    "Investing",
    "Personal Finance",
    "Business",
    "Technology",
    "Science",
    "Health",
    "World",
  ]

  const newsArticles = [
    {
      id: 1,
      title: "Market Volatility Continues Amidst Economic Uncertainty",
      description:
        "Investors remain cautious as market fluctuations persist, driven by concerns over inflation and interest rate hikes.",
      image: "/images/market-chart.jpg",
    },
    {
      id: 2,
      title: "Tech Sector Shows Resilience Despite Broader Market Downturn",
      description:
        "Despite overall market challenges, the technology sector demonstrates stability, with some companies reporting positive earnings.",
      image: "/images/tech-building.jpg",
    },
    {
      id: 3,
      title: "Consumer Spending Remains Strong, Boosting Retail Sales",
      description:
        "Robust consumer spending continues to support the economy, leading to increased sales in the retail sector.",
      image: "/images/retail-store.jpg",
    },
    {
      id: 4,
      title: "Global Trade Talks Stall as Tensions Rise",
      description:
        "International trade negotiations face setbacks due to escalating geopolitical tensions and disagreements over tariffs.",
      image: "/images/globe.jpg",
    },
    {
      id: 5,
      title: "Central Bank Announces New Monetary Policy",
      description:
        "The central bank introduces a new monetary policy aimed at stabilizing the economy and managing inflation.",
      image: "/images/bank.jpg",
    },
    {
      id: 6,
      title: "Unemployment Rate Drops to Record Low",
      description:
        "The national unemployment rate reaches a historic low, indicating a strong labor market and economic growth.",
      image: "/images/employment.jpg",
    },
  ]

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      {/* Top Navigation */}
      <header className="border-b border-slate-700 bg-slate-800">
        <div className="flex items-center justify-between px-6 py-4">
          <div className="flex items-center space-x-8">
            <div className="flex items-center space-x-2">
              <Globe className="h-6 w-6" />
              <span className="text-xl font-bold">News</span>
            </div>
            <nav className="hidden md:flex space-x-6">
              <a href="#" className="text-gray-300 hover:text-white transition-colors">
                World
              </a>
              <a href="#" className="text-gray-300 hover:text-white transition-colors">
                Business
              </a>
              <a href="#" className="text-gray-300 hover:text-white transition-colors">
                Tech
              </a>
              <a href="#" className="text-gray-300 hover:text-white transition-colors">
                Science
              </a>
              <a href="#" className="text-gray-300 hover:text-white transition-colors">
                Health
              </a>
            </nav>
          </div>
        </div>
      </header>

      <div className="flex">
        {/* Left Sidebar */}
        <aside className="w-80 p-6 border-r border-slate-700">
          {/* Search Box */}
          <div className="relative mb-8">
            <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
            <Input
              placeholder="Search"
              className="pl-10 bg-slate-700 border-slate-600 text-white placeholder-gray-400"
            />
          </div>

          {/* Popular Searches */}
          <div className="mb-8">
            <h3 className="text-lg font-semibold mb-4">Popular Searches</h3>
            <div className="space-y-2">
              {popularSearches.map((search, index) => (
                <Button
                  key={index}
                  variant="secondary"
                  className="w-full justify-start bg-slate-700 hover:bg-slate-600 text-left"
                >
                  {search}
                </Button>
              ))}
            </div>
          </div>

          {/* News Categories */}
          <div>
            <h3 className="text-lg font-semibold mb-4">News Categories</h3>
            <div className="flex flex-wrap gap-2">
              {newsCategories.map((category, index) => (
                <Button key={index} variant="secondary" size="sm" className="bg-slate-700 hover:bg-slate-600">
                  {category}
                </Button>
              ))}
            </div>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-6">
          {/* Hero Section */}
          <div className="mb-8">
            <div className="relative h-64 bg-gradient-to-r from-teal-500 to-emerald-500 rounded-lg overflow-hidden">
              <img src="/images/hero-mockup.png" alt="Website mockup" className="object-cover w-full h-full" />
              <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex space-x-2">
                <div className="w-2 h-2 bg-white rounded-full"></div>
                <div className="w-2 h-2 bg-white/50 rounded-full"></div>
                <div className="w-2 h-2 bg-white/50 rounded-full"></div>
                <div className="w-2 h-2 bg-white/50 rounded-full"></div>
              </div>
            </div>
          </div>

          {/* Latest News */}
          <section>
            <h2 className="text-2xl font-bold mb-6">Latest News</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {newsArticles.map((article) => (
                <article
                  key={article.id}
                  className="bg-slate-800 rounded-lg overflow-hidden hover:bg-slate-750 transition-colors"
                >
                  <div className="relative h-48">
                    <img
                      src={article.image || "https://via.placeholder.com/300x200"}
                      alt={article.title}
                      className="object-cover w-full h-full"
                    />
                  </div>
                  <div className="p-4">
                    <h3 className="font-semibold text-lg mb-2 line-clamp-2">{article.title}</h3>
                    <p className="text-gray-400 text-sm line-clamp-3">{article.description}</p>
                  </div>
                </article>
              ))}
            </div>
          </section>
        </main>
      </div>
    </div>
  )
}

export default App
