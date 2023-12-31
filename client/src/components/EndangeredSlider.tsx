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
import WaterQuality from "./WaterQuality";

const images = ["cat1.jpg", "cat2.jpg", "cat3.jpg", "cat4.jpg"];

type EndangeredSliderProps = {
    Id: number;
    "Scientific Name": string;
    "Common Name": string;
    Salinity: string;
    Resilience: string;
    "Fishing Vulnerability": string;
    "IUCN Red List Status": string;
    "Threats To Humans": string;
};

const EndangeredSlider = (WaterQuality: any) => {
    // Effect to fetch data when the component mounts
    const [endangeredSpecies, setEndangeredSpecies] = useState<
        EndangeredSliderProps[]
    >([]);
    const [isOpen, setIsOpen] = useState(false);
    const name = WaterQuality.waterQuality.name;
    console.log(name)
    useEffect(() => {
        (async () => {
            // Define the URL for the API endpoint
            const apiUrl = `http://127.0.0.1:8000/animals/get_endangered_species_data/${name}`;
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
    }, [WaterQuality.waterQuality.name]);
    return (
        <Card>
            <CardHeader>
                <CardTitle>Endangered Species</CardTitle>
            </CardHeader>
            <CardContent style={{ height: "80px" }}>
                <div className="flex overflow-x-auto">
                    {endangeredSpecies?.map((species, key) => (
                        <Dialog key={key}>
                            <DialogTrigger>
                                {!species["Threats To Humans"] ? (
                                    <Button variant="destructive" onClick={() => setIsOpen(true)}>
                                        {species["Common Name"]}
                                    </Button>
                                ) : (
                                    <Button variant="secondary" onClick={() => setIsOpen(true)}>
                                        {species["Common Name"]}
                                    </Button>
                                )}
                            </DialogTrigger>
                            <DialogContent>
                                <DialogHeader>
                                    <DialogTitle>{species["Common Name"]}</DialogTitle>
                                </DialogHeader>
                                <DialogDescription>
                                    <ul>
                                        {species["IUCN Red List Status"] !== "Not Evaluated" ? (
                                            <li>
                                                Endangered Status: {species["IUCN Red List Status"]}
                                            </li>
                                        ) : null}
                                        <li><strong>Scientist Name</strong>: {species["Scientific Name"]}</li>
                                        <li><strong>Threat to Humans</strong>: {species["Threats To Humans"]}</li>
                                        <li><strong>Resilience</strong>: {species["Resilience"]}</li>
                                        <li><strong>Salinity</strong>: {species["Salinity"]}</li>
                                        <li>
                                            <strong>Fishing Vulnerability</strong>: {species["Fishing Vulnerability"]}
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
