import { createTheme } from '@mui/material/styles';
import { red } from '@mui/material/colors';

// A custom theme for this app
const theme = createTheme({
    palette: {
        primary: {
            main: '#a142ff',
        },
        secondary: {
            main: '#5c61ff',
        },
        error: {
            main: red.A400,
        },
    },
});

export default theme;