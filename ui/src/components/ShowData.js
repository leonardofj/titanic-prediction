import React, { useEffect, useState } from 'react';
import axios from "axios";
import {
    Box,
    Table,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    TableContainer,
} from '@chakra-ui/react'

export default function ShowData() {
    const [data, setData] = useState([{}]);

    useEffect(() => {
        axios.get("http://localhost:5000/api/list-data")
            .then(res => {
                setData(res.data);
            })
    }, []);

    return (
        <Box >
            <TableContainer width="100%" overflowX="hidden">
                <Table size='sm' variant='striped' colorScheme='gray'>
                    <Thead>
                        <Tr>
                            {Object.keys(data[0]).map((key) => (
                                <Th>{key.split('_').join(' ')}</Th>
                            ))}
                        </Tr>
                    </Thead>
                    <Tbody>
                        {data.map((item) => (
                            <Tr key={item.id}>
                                {Object.values(item).map((val) => (
                                    <Td>{val === null ? "" : String(val)}</Td>
                                ))}
                            </Tr>
                        ))}
                    </Tbody>
                </Table>
            </TableContainer>
        </Box>
    );
}
