import { render, screen } from '@testing-library/react';
import { vi } from 'vitest';
import App from './App';
import axios from 'axios';

import type { MockedFunction } from 'vitest';

vi.mock('axios');

test('renders App component and mocks API call', async () => {
  (axios.get as MockedFunction<typeof axios.get>).mockResolvedValue({ data: 'Hello from API' });

  render(<App />);

  expect(screen.getByText(/hello/i)).toBeInTheDocument();
});
