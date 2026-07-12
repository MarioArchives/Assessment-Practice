import { useState, useCallback } from 'react';
import { Post, fetchPosts, FetchPostsResult } from './mockApi';

// Suppress unused import warnings — candidates will use these
void fetchPosts;
void ({} as FetchPostsResult);
void ({} as Post);

export interface FeedProps {
  pageSize?: number;
}

// TODO: implement a proper spinner (currently just a placeholder)
function LoadingSpinner() {
  return (
    <div role="status" aria-label="Loading more posts">
      {/* TODO: replace with a real CSS spinner */}
      <span>Loading…</span>
    </div>
  );
}

// TODO: implement InfiniteScrollFeed
export default function InfiniteScrollFeed(_props: FeedProps) {
  const [_posts, _setPosts] = useState<Post[]>([]);

  // TODO: track loading state
  // TODO: track whether more pages exist
  // TODO: track the current page number
  // TODO: track fetch errors

  // TODO: write a loadPage function that calls fetchPosts and updates state

  // TODO: attach an IntersectionObserver to a sentinel element using
  //       the useCallback ref pattern so it fires loadPage when the
  //       sentinel enters the viewport (rootMargin: '200px')
  const _sentinelRef = useCallback((_node: HTMLDivElement | null) => {
    // TODO: create and attach the IntersectionObserver here
    // TODO: return a cleanup function that disconnects the observer
  }, []);

  return (
    <div>
      {/* TODO: render the list of post cards */}
      {/* TODO: render LoadingSpinner while fetching */}
      {/* TODO: render an error message + retry button on failure */}
      {/* TODO: render "No more posts" when the feed is exhausted */}
      {/* TODO: render the sentinel <div> with _sentinelRef */}
      <p>InfiniteScrollFeed – not yet implemented</p>
    </div>
  );
}
