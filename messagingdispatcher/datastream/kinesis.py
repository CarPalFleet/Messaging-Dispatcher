import boto3

class Kinesis(object):
    def __init__(self):
        self._client = boto3.client('kinesis')

    def put_record(self, stream_name, data, key):
        return self._client.put_record(StreamName=stream_name,
                                       Data=data,
                                       PartitionKey=key)

    def get_records(self, stream_name):
        shard_iterator = self._client.get_shard_iterator(
            StreamName=stream_name,
            ShardId='shardId-000000000000',
            ShardIteratorType='LATEST'
        ).get('ShardIterator')
        return self._client.get_records(ShardIterator=shard_iterator)