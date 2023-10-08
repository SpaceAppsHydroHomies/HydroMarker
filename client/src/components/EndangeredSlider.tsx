import { Card, CardContent, CardHeader, CardTitle } from "./ui/card";
import { useEffect, useState } from "react"

const images = ["cat1.jpg", "cat2.jpg", "cat3.jpg", "cat4.jpg"];

const EndangeredSlider = () => {

    // Effect to fetch data when the component mounts
    useEffect(() => {
        // Define the URL for the API endpoint
        const apiUrl = 'http://127.0.0.1:8000/animals/get_endangered_species_data/Gulf%20of%20Mexico/';

        // Fetch data from the API using the fetch() function
        fetch(apiUrl)
            .then((response) => response.json())
            .then((responseData) => {
                console.log(responseData)
            })
            .catch((error) => {
                console.error('Error fetching data:', error);
            });
    }, []);
    return (
        <Card>
            <CardHeader>
                <CardTitle>Endangered Species</CardTitle>
            </CardHeader>
            <CardContent>
                <div className="flex overflow-x-auto">
                    {images.map((image) => (
                        <img
                            className="w-52 h-52 rounded-xl object-cover"
                            src={`/${image}`}
                            alt="cat"
                        />
                    ))}
                </div>
            </CardContent>
        </Card>
    );
};

export default EndangeredSlider;
