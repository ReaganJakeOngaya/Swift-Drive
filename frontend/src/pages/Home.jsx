import { useEffect, useState } from "react";
import API from "../api/axios";

export default function Home() {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    API.get("/cars")
      .then(res => setCars(res.data))
      .catch(() => alert("Failed to load cars"));
  }, []);

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-4">🏎️ Sports Cars for Sale</h1>
      <div className="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
        {cars.map(car => (
          <div key={car.id} className="bg-white p-4 rounded shadow">
            <img src={car.image_url} alt={car.name} className="w-full h-48 object-cover rounded" />
            <h2 className="text-xl font-semibold mt-2">{car.brand} - {car.name}</h2>
            <p className="text-gray-700">${car.price.toLocaleString()}</p>
            <p className="text-sm text-gray-500 mt-1">{car.description?.slice(0, 60)}...</p>
          </div>
        ))}
      </div>
    </div>
  );
}
