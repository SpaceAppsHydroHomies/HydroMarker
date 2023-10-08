import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { useEffect, useState } from "react";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "./ui/dialog";
import { Button } from "./ui/button";

const images = ["cat1.jpg", "cat2.jpg", "cat3.jpg", "cat4.jpg"];

type EndangeredSliderProps = {
  id: number;
  scientificName: string;
  commonName: string;
  salinity: string;
  resilience: string;
  fishingVulnerability: string;
  IUCN: string;
  threatToHumans: string;
};

const EndangeredSlider = () => {
  // Effect to fetch data when the component mounts
  const [endangeredSpecies, setEndangeredSpecies] = useState<
    EndangeredSliderProps[]
  >([]);
  const [isOpen, setIsOpen] = useState(false);
  useEffect(() => {
    (async () => {
      // Define the URL for the API endpoint
      const apiUrl =
        "http://127.0.0.1:8000/animals/get_endangered_species_data/Alabama%20River";
      try {
        // Fetch data from the API using the fetch() function
        const data = await fetch(apiUrl)
          .then((response) => response.json())
          .then((responseData) => {
            // Set the state variable using the data returned from the API
            setEndangeredSpecies(responseData["Endangered Species"]);
          });
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    })();
  }, []);
  return (
    <Card>
      <CardHeader>
        <CardTitle>Endangered Species</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex overflow-x-auto">
          {endangeredSpecies.map((species, key) => (
            <Dialog>
              <DialogTrigger>
                {!species.threatToHumans ? (
                  <Button variant="destructive" onClick={() => setIsOpen(true)}>
                    {species.commonName}
                  </Button>
                ) : (
                  <Button variant="secondary" onClick={() => setIsOpen(true)}>
                    {species.commonName}
                  </Button>
                )}
              </DialogTrigger>
              <DialogContent>
                <DialogHeader>
                  <DialogTitle key={key}>{species.commonName}</DialogTitle>
                </DialogHeader>
                <DialogDescription>
                  <ul>
                    {species.IUCN !== "Not Evaluated" ? (
                      <li>Endangered Status: {species.IUCN}</li>
                    ) : null}
                    <li>Scientist Name: {species.scientificName}</li>
                    <li>Threat to Humans: {species.threatToHumans}</li>
                    <li>Resilience: {species.resilience}</li>
                    <li>Salinity: {species.salinity}</li>
                    <li>
                      Fishing Vulnerability: {species.fishingVulnerability}
                    </li>
                  </ul>
                </DialogDescription>
              </DialogContent>
            </Dialog>
          ))}
        </div>
      </CardContent>
    </Card>
  );
};

export default EndangeredSlider;
