import { Helmet } from "react-helmet";

import Header from "./components/Header";
import MainContent from "./components/MainContent";
import { ThemeProvider } from "./components/theme-provider";
import Map from "./components/Map";
import { useState } from "react";
import SearchDialog from "./components/SearchDialog";

function App() {
  const [isSearchDialogOpen, setIsSearchDialogOpen] = useState(false);
  return (
    <>
      <Helmet>
        <title>WaterTime :3</title>
        <link rel="icon" href="/favicon_io/favicon.ico" />
        <link rel="apple-touch-icon" href="/favicon_io/apple-touch-icon.png" />
        <link rel="manifest" href="/favicon_io/site.webmanifest" />
      </Helmet>
      <ThemeProvider>
        <body className="container min-h-screen">
          <Header />
          <MainContent />
        </body>
      </ThemeProvider>
      <Map />
      <SearchDialog
        open={isSearchDialogOpen}
        onClose={() => setIsSearchDialogOpen(!isSearchDialogOpen)}
      />
    </>
  );
}

export default App;
