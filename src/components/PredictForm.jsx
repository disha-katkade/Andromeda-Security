import React, { useState } from 'react';
import axios from 'axios';

const PredictForm = () => {
    const [features, setFeatures] = useState({
        feature1: '',
        feature2: '',
        feature3: '',
        feature4: '',
        feature5: ''
    });

    const [result, setResult] = useState('');

    const handleChange = (e) => {
        setFeatures({ ...features, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/predict', {
                features: [
                    parseFloat(features.feature1),
                    parseFloat(features.feature2),
                    parseFloat(features.feature3),
                    parseFloat(features.feature4),
                    parseFloat(features.feature5)
                ]
            });
            setResult(response.data.prediction);
        } catch (error) {
            console.error('Prediction failed:', error);
            setResult('Error occurred');
        }
    };

    return (
        <div>
            <h2>Transaction Prediction</h2>
            <form onSubmit={handleSubmit}>
                {Object.keys(features).map((key) => (
                    <div key={key}>
                        <label>{key}: </label>
                        <input
                            type="number"
                            name={key}
                            value={features[key]}
                            onChange={handleChange}
                        />
                    </div>
                ))}
                <button type="submit">Predict</button>
            </form>
            <h3>Result: {result}</h3>
        </div>
    );
};

export default PredictForm;
