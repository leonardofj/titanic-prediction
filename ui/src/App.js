import React from 'react';
import {
  ChakraProvider,
  Box,
  Text,
  VStack,
  Grid,
  Tabs, TabList, TabPanels, Tab, TabPanel,
  theme,
} from '@chakra-ui/react';
import Prediction from './components/Prediction';
import ShowData from './components/ShowData';

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Box textAlign="center" fontSize="xl">
        <Grid minH="50vh" p={3}>
          <VStack spacing={7}>
            <Text
              color="teal.500"
              fontSize="2xl"
            >
              Titanic prediction app
            </Text>
          </VStack>
          <Tabs>
            <TabList>
              <Tab>Prediction</Tab>
              <Tab>Show data</Tab>
            </TabList>

            <TabPanels>
              <TabPanel>
                <Prediction />
              </TabPanel>
              <TabPanel>
                <ShowData />
              </TabPanel>
            </TabPanels>
          </Tabs>
        </Grid>
      </Box>
    </ChakraProvider>
  );
}

export default App;
