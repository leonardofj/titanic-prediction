import React from 'react';
import {
  ChakraProvider,
  Box,
  Grid,
  Tabs,
  TabList,
  TabPanels,
  Tab,
  TabPanel,
  theme,
} from '@chakra-ui/react';
import Prediction from './components/Prediction';
import ShowData from './components/ShowData';

function App() {
  return (
    <ChakraProvider theme={theme}>
      <Box >
        <Grid minH="50vh" p={3}>
          <Box width="100%" height={60} bgImage='/header.png' bgPosition="top-left"
            bgRepeat="no-repeat">
            <Box p='4' textAlign="left" textColor="blue.500" fontSize="3xl" as='b'>
              Titanic survival prediction
            </Box>
          </Box>
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
