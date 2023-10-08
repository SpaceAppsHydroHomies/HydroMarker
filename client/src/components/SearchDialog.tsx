import {
    Command,
    CommandDialog,
    CommandEmpty,
    CommandGroup,
    CommandInput,
    CommandItem,
    CommandList,
    CommandSeparator,
} from "@/components/ui/command";
import { useEffect, useState } from "react";

function SearchDialog ({
    open,
    onClose,
}: {
    open: boolean;
    onClose: () => void;
}) {
    const [searchResults, setSearchResults] = useState<
        searchResultsProps[]
    >([]);
    useEffect(() => {
        (async () => {
            // Define the URL for the API endpoint
            const apiUrl =
                "http://127.0.0.1:8000/animals/get_ecosystems/";
            try {
                // Fetch data from the API using the fetch() function
                const data = await fetch(apiUrl)
                    .then((response) => response.json())
                    .then((responseData) => {
                        // Set the state variable using the data returned from the API
                        setSearchResults(responseData["Ecosystems"]);
                    });
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        })();
    }, []);
    return (
        <CommandDialog open={open} onOpenChange={onClose}>
            <CommandInput placeholder="Search for a body of water" />
            <CommandList>
                <CommandEmpty>No results found.</CommandEmpty>
                <CommandGroup heading="Suggestions">
                    {searchResults.map((results, key) => (
                        <CommandItem key={key}>{results}</CommandItem>
                    ))}
                    <CommandItem>sdsd</CommandItem>
                </CommandGroup>
                <CommandSeparator />
            </CommandList>
        </CommandDialog>
    );
}

export default SearchDialog;
