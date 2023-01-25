import React, { useState } from 'react';
import axios from "axios";
import {
    Box,
    Text,
    Button,
    useToast,
    Radio,
    RadioGroup,
    Stack,
    Select,
    FormControl,
    FormLabel,
    NumberInput,
    NumberInputField,
    NumberInputStepper,
    NumberIncrementStepper,
    NumberDecrementStepper
} from '@chakra-ui/react'

export default function Prediction() {
    const [pclass, setPclass] = useState('1');
    const [gender, setGender] = useState('male');
    const [age, setAge] = useState(0);
    const [survived, setSurvived] = useState('');
    const [accuracy, setAccuracy] = useState('');
    const toast = useToast();

    const handleSubmit = (event) => {
        event.preventDefault();
        // calling the api
        axios.get("http://localhost:5000/api/make-prediction", {
            params: {
                gender: gender,
                class: parseInt(pclass),
                age: age ? age : 0
            }
        })
            .then(res => {
                if (!res.data.survived) {
                    toast({
                        title: 'Prediction is unfortunate',
                        status: 'error',
                        duration: 3000,
                        position: "top",
                        isClosable: true,
                    });
                }
                setSurvived(res.data.survived);
                setAccuracy(res.data.accuracy)
            })
    };

    return (
        <Stack spacing={40} direction='row'>
            <Box>
                <form onSubmit={handleSubmit}>
                    <FormControl>
                        <FormLabel>Gender</FormLabel>
                        <RadioGroup name="gender" onChange={setGender} value={gender}>
                            <Stack direction='row'>
                                <Radio name="gender" value='male'>Male</Radio>
                                <Radio name="gender" value='female'>Female</Radio>
                            </Stack>
                        </RadioGroup>
                    </FormControl>
                    <br />
                    <FormControl>
                        <FormLabel>Class</FormLabel>
                        <Select name="class" value={pclass} onChange={(e) => setPclass(e.target.value)}>
                            <option value='1'>First class</option>
                            <option value='2'>Second class</option>
                            <option value='3'>Third class</option>
                        </Select>
                    </FormControl>
                    <br />
                    <FormControl>
                        <FormLabel>Age</FormLabel>
                        <NumberInput name="age" value={age} max={120} min={0} onChange={(value) => setAge(value)}>
                            <NumberInputField />
                            <NumberInputStepper>
                                <NumberIncrementStepper />
                                <NumberDecrementStepper />
                            </NumberInputStepper>
                        </NumberInput>
                    </FormControl>
                    <br />
                    <Button type='submit' colorScheme='blue'>Predict</Button>
                </form>
            </Box>
            <Box width="100%">
                {survived === "" ? "" :
                    <Box width="100%" height="100%" textAlign="center" fontSize="5xl" as='b'>
                        {survived ? <Box width="100%" height={80} p="3" bgImage='/rose.jpg' bgPosition="left"
                            bgRepeat="no-repeat">
                            <Text textAlign="left" textColor="lime">Survive</Text>
                        </Box> :
                            <Box width="100%" height={80} p="3" bgImage='/jack.jpg' bgPosition="left"
                                bgRepeat="no-repeat">
                                <Text textAlign="left" textColor="red">Not survive</Text>
                            </Box>}
                        <Text textAlign="left" fontSize="xl">Accuracy: {accuracy}</Text>
                    </Box>}
            </Box>
        </Stack >
    );
}
