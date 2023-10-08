import { FaSearchLocation } from "react-icons/fa";

import { ModeToggle } from "./mode-toggle";
import { Button } from "./ui/button";

const Header = () => {
  return (
    <div className="flex justify-between py-3">
      <img src="/favicon_io/favicon.ico" alt="logo" className="w-10 h-10" />
      <div className="flex gap-2">
        <Button variant="outline" size="icon">
          <FaSearchLocation />
        </Button>
        <ModeToggle />
      </div>
    </div>
  );
};

export default Header;
