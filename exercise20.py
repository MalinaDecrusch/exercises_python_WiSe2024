{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ff27c0f2",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'data/Daten-20241205.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 9\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m file_name  \u001b[38;5;129;01min\u001b[39;00m file_names:\n\u001b[0;32m      8\u001b[0m     file_path \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mdata/Daten-20241205.csv\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m----> 9\u001b[0m     data_frames[file_name] \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(file_path)\n\u001b[0;32m     11\u001b[0m aapl_data \u001b[38;5;241m=\u001b[39m data_frames[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAAPL\u001b[39m\u001b[38;5;124m'\u001b[39m][[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mDate\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mClose\u001b[39m\u001b[38;5;124m'\u001b[39m]]\u001b[38;5;241m.\u001b[39mrename(\n\u001b[0;32m     12\u001b[0m     columns \u001b[38;5;241m=\u001b[39m {\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mClose\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mAAPL\u001b[39m\u001b[38;5;124m'\u001b[39m})\n\u001b[0;32m     13\u001b[0m goog_data \u001b[38;5;241m=\u001b[39m data_frames[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mGOOG\u001b[39m\u001b[38;5;124m'\u001b[39m][[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mDate\u001b[39m\u001b[38;5;124m'\u001b[39m, \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mClose\u001b[39m\u001b[38;5;124m'\u001b[39m]]\u001b[38;5;241m.\u001b[39mrename(\n\u001b[0;32m     14\u001b[0m     columns \u001b[38;5;241m=\u001b[39m {\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mClose\u001b[39m\u001b[38;5;124m'\u001b[39m:\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mGOOG\u001b[39m\u001b[38;5;124m'\u001b[39m})\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:912\u001b[0m, in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[0m\n\u001b[0;32m    899\u001b[0m kwds_defaults \u001b[38;5;241m=\u001b[39m _refine_defaults_read(\n\u001b[0;32m    900\u001b[0m     dialect,\n\u001b[0;32m    901\u001b[0m     delimiter,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    908\u001b[0m     dtype_backend\u001b[38;5;241m=\u001b[39mdtype_backend,\n\u001b[0;32m    909\u001b[0m )\n\u001b[0;32m    910\u001b[0m kwds\u001b[38;5;241m.\u001b[39mupdate(kwds_defaults)\n\u001b[1;32m--> 912\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m _read(filepath_or_buffer, kwds)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:577\u001b[0m, in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    574\u001b[0m _validate_names(kwds\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnames\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    576\u001b[0m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[1;32m--> 577\u001b[0m parser \u001b[38;5;241m=\u001b[39m TextFileReader(filepath_or_buffer, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwds)\n\u001b[0;32m    579\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[0;32m    580\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1407\u001b[0m, in \u001b[0;36mTextFileReader.__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m   1404\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m kwds[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m   1406\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles: IOHandles \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m-> 1407\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_engine \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_make_engine(f, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mengine)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1661\u001b[0m, in \u001b[0;36mTextFileReader._make_engine\u001b[1;34m(self, f, engine)\u001b[0m\n\u001b[0;32m   1659\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m mode:\n\u001b[0;32m   1660\u001b[0m         mode \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1661\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;241m=\u001b[39m get_handle(\n\u001b[0;32m   1662\u001b[0m     f,\n\u001b[0;32m   1663\u001b[0m     mode,\n\u001b[0;32m   1664\u001b[0m     encoding\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mencoding\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1665\u001b[0m     compression\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcompression\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1666\u001b[0m     memory_map\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmemory_map\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mFalse\u001b[39;00m),\n\u001b[0;32m   1667\u001b[0m     is_text\u001b[38;5;241m=\u001b[39mis_text,\n\u001b[0;32m   1668\u001b[0m     errors\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mencoding_errors\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstrict\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m   1669\u001b[0m     storage_options\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstorage_options\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1670\u001b[0m )\n\u001b[0;32m   1671\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1672\u001b[0m f \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles\u001b[38;5;241m.\u001b[39mhandle\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\pandas\\io\\common.py:859\u001b[0m, in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    854\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m    855\u001b[0m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[0;32m    856\u001b[0m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[0;32m    857\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mencoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mmode:\n\u001b[0;32m    858\u001b[0m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[1;32m--> 859\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(\n\u001b[0;32m    860\u001b[0m             handle,\n\u001b[0;32m    861\u001b[0m             ioargs\u001b[38;5;241m.\u001b[39mmode,\n\u001b[0;32m    862\u001b[0m             encoding\u001b[38;5;241m=\u001b[39mioargs\u001b[38;5;241m.\u001b[39mencoding,\n\u001b[0;32m    863\u001b[0m             errors\u001b[38;5;241m=\u001b[39merrors,\n\u001b[0;32m    864\u001b[0m             newline\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    865\u001b[0m         )\n\u001b[0;32m    866\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    867\u001b[0m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[0;32m    868\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(handle, ioargs\u001b[38;5;241m.\u001b[39mmode)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'data/Daten-20241205.csv'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_names = ['AAPL', 'GOOG', 'META', 'MSFT']\n",
    "\n",
    "data_frames = {}\n",
    "\n",
    "for file_name  in file_names:\n",
    "    file_path = f'data/Daten-20241205.csv'\n",
    "    data_frames[file_name] = pd.read_csv(file_path)\n",
    "    \n",
    "aapl_data = data_frames['AAPL'][['Date', 'Close']].rename(\n",
    "    columns = {'Close':'AAPL'})\n",
    "goog_data = data_frames['GOOG'][['Date', 'Close']].rename(\n",
    "    columns = {'Close':'GOOG'})\n",
    "meta_data = data_frames['META'][['Date', 'Close']].rename(\n",
    "    columns = {'Close':'META'})\n",
    "msft_data = data_frames['MSFT'][['Date', 'Close']].rename(\n",
    "    columns = {'Close':'MSFT'})\n",
    "\n",
    "merged_data_AG = pd.merge(aapl_data, goog_data, on = 'Date', how='outer')\n",
    "merged_data_AGM = pd.merge(pd.merged_data_AG, meta_data, on ='date', how ='outer')\n",
    "df_final = pd.merge(\n",
    "    merged_data_AGM, msft_data, on ='Date', how = \"outer\")\n",
    "df_finale = df_final.reset_index(drop=True)\n",
    "df_final.head() \n",
    "df_final.to_csv('data/stocks.csv', sep = ',', decimal ='.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5427558c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
