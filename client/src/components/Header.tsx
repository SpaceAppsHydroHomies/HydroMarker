import { FaSearchLocation } from "react-icons/fa";

import { ModeToggle } from "./mode-toggle";
import { Button } from "./ui/button";
import SearchDialog from "./SearchDialog";
import { useState } from "react";

const Header = () => {
  const [open, setOpen] = useState(false);
  return (
    <div className="flex justify-between py-3">
      <img src="/favicon_io/favicon.ico" alt="logo" className="w-10 h-10" />
      <div className="flex gap-2">
        <Button variant="outline" size="icon" onClick={() => setOpen(!open)}>
          <FaSearchLocation />
        </Button>
        <ModeToggle />
      </div>
      <SearchDialog open={open} onClose={() => setOpen(false)} />
    </div>
  );
};

export default Header;
