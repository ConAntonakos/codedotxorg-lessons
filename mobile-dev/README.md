# Introduction to Mobile Development with React Native

In this guide, we’ll start from scratch and follow a step-by-step approach to learning React Native. We will use internet searches to solve problems, just like a developer would do.

## Step 1: Install Node.js and npm

React Native requires **Node.js** and **npm** (Node Package Manager) to work.

1. **Search for "How to install Node.js"** on your preferred search engine.
2. Visit the official [Node.js website](https://nodejs.org/) and download the latest LTS version.
3. Install it, and make sure to include npm (it comes bundled with Node.js).

### Verification:
1. Open your terminal (or command prompt).
2. Type `node -v` to verify Node.js is installed.
3. Type `npm -v` to verify npm is installed.

## Step 2: Install React Native CLI

To start building React Native apps, you'll need to install the React Native CLI (Command Line Interface).

1. **Search for "How to install React Native CLI"**.
2. Run the following command in your terminal:

    ```bash
    npm install -g react-native-cli
    ```

3. After installation, verify it by running:

    ```bash
    react-native --version
    ```

## Step 3: Install Xcode and Android Studio

React Native apps require Android and iOS emulators for testing.

1. **Search for "How to install Xcode"** (for macOS users).
   - Xcode is required to run iOS simulators. Install it from the App Store.
2. **Search for "How to install Android Studio"** (for both Windows and macOS users).
   - Download Android Studio from [here](https://developer.android.com/studio).
   - Follow the instructions to set up the Android emulator.

### Verification:
1. Launch Xcode or Android Studio to ensure that the emulators are working properly.

## Step 4: Create Your First React Native Project

Now let’s create a simple React Native app.

1. **Search for "How to create a React Native project"**.
2. Run the following command to create a new React Native app:

    ```bash
    npx react-native init MyFirstApp
    ```

3. After the project is created, navigate to the project folder:

    ```bash
    cd MyFirstApp
    ```

4. **Search for "How to run React Native app on emulator"** to find the steps for running it on an Android or iOS emulator.
   - For Android:

     ```bash
     npx react-native run-android
     ```

   - For iOS (macOS only):

     ```bash
     npx react-native run-ios
     ```

### Result:
You should see your React Native app running in the emulator.

## Step 5: Learn Basic React Native Components

React Native uses various built-in components for building user interfaces.

1. **Search for "React Native basic components"**.
2. Learn about the `View`, `Text`, `Image`, `TextInput`, and `Button` components.

### Example:
```javascript
import React from 'react';
import { View, Text, Button } from 'react-native';

const App = () => {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Hello, React Native!</Text>
      <Button title="Click Me" onPress={() => alert('Button clicked!')} />
    </View>
  );
};

export default App;
