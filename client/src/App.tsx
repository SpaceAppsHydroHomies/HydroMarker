import { Helmet } from "react-helmet";

import Header from "./components/Header";
import MainContent from "./components/MainContent";
import { ThemeProvider } from "./components/theme-provider";
import Map from "./components/Map";
import { useState } from "react";
import SearchDialog from "./components/SearchDialog";

function App() {
  const [isSearchDialogOpen, setIsSearchDialogOpen] = useState(false);
  const [longlati, setLonglati] = useState<LatLng>({
    lat: 37.719,
    lng: -97.293,
  });
  return (
    <>
      <Helmet>
        <title>WaterTime :3</title>
        <link rel="icon" href="/favicon_io/favicon.ico" />
        <link rel="apple-touch-icon" href="/favicon_io/apple-touch-icon.png" />
        <link rel="manifest" href="/favicon_io/site.webmanifest" />
      </Helmet>
      <ThemeProvider>
        <div className="container min-h-screen">
          <Header />
          <MainContent longlati={longlati} />
        </div>
      </ThemeProvider>
      <div>
        <Map longlati={longlati} setLonglati={setLonglati} />
      </div>
      <SearchDialog
        open={isSearchDialogOpen}
        onClose={() => setIsSearchDialogOpen(!isSearchDialogOpen)}
      />
    </>
  );
}

export default App;
