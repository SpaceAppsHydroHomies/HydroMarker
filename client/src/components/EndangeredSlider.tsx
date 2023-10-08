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

// type EndangeredSliderProps = {
//     Id: number;
//     "Scientific Name": string;
//     "Common Name": string;
//     Salinity: string;
//     Resilience: string;
//     "Fishing Vulnerability": string;
//     "IUCN Red List Status": string;
//     "Threats To Humans": string;
// };

type EndangeredSliderProps = {
    name: "Arkansas River"
};


const EndangeredSlider: React.FC<EndangeredSliderProps> = ({ name }) => {
    name = "Arkansas River"
    // Effect to fetch data when the component mounts
    const [endangeredSpecies, setEndangeredSpecies] = useState<
        EndangeredSliderProps[]
    >([]);
    const [isOpen, setIsOpen] = useState(false);
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
    }, []);
    return (
        <Card>
            <CardHeader>
                <CardTitle>Endangered Species</CardTitle>
            </CardHeader>
            <CardContent>
                <div className="flex overflow-x-auto">
                    {endangeredSpecies.map((species, key) => (
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
                                            <li>Endangered Status: {species["IUCN Red List Status"]}</li>
                                        ) : null}
                                        <li>Scientist Name: {species["Scientific Name"]}</li>
                                        <li>Threat to Humans: {species["Threats To Humans"]}</li>
                                        <li>Resilience: {species["Resilience"]}</li>
                                        <li>Salinity: {species["Salinity"]}</li>
                                        <li>Fishing Vulnerability: {species["Fishing Vulnerability"]}</li>
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
