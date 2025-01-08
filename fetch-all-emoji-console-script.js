async function fetchAllEmoji() {
	let emoji = [];
	for(let page = 1; page < 100; page++) {
		const fd = new FormData();
		fd.append('page', page);
		fd.append('count', 200);
		fd.append('token', boot_data.api_token);
		console.log(`Fetching page ${page}`);
		const resp = await fetch('/api/emoji.adminList', {credentials: "include", method: "POST", body: fd});
		const json = await resp.json();
		const pEmoji = json.emoji || [];
		emoji = emoji.concat(pEmoji);
		if(!pEmoji.length) break;
	}
	console.log(`Fetched ${emoji.length} emoji!`);
	return emoji;
}
copy(await fetchAllEmoji());
