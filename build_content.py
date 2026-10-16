"""Build a dated, source-linked hockey field guide from saved official NHL data."""
import json, re
from pathlib import Path

ROOT=Path(__file__).parent
OUT=ROOT/'docs'
def load(name): return json.loads((ROOT/'research'/name).read_text(encoding='utf-8'))
def paras(s): return [p.strip() for p in s.strip().split('\n\n') if p.strip()]
lessons=[]
def lesson(slug,title,deck,text,exercise,category='Hockey from zero'):
    lessons.append(dict(id=slug,title=title,deck=deck,paragraphs=paras(text),exercise=exercise,category=category))

lesson('start','01 · You already belong here','A way into the game, without homework anxiety.', '''
Welcome to the Vibes Hockey Club. Five friends, five teams, and absolutely no requirement to justify how you chose yours. Picking a team because the name, colours, city or general emotional weather feels right is a perfectly respectable beginning. The useful next step is learning what you are looking at. This course starts from zero, then gives Montreal extra attention and introduces Minnesota, Pittsburgh, Ottawa and Seattle. You can read in order or dip into a team guide.

The first thing to know is that hockey is a game about making time and space disappear. A player who has the puck wants enough of both to do something useful. The defending team wants to take them away. Skating, passing, checking and positioning are different tools for that same contest. A beautiful pass matters because it reaches somebody before the defenders can adjust. A good defensive play may look uneventful because it prevents the exciting thing from happening.

You do not need to see the puck continuously. Even experienced fans lose it. Watch the players' heads, the direction their sticks point and the camera movement. When a pass disappears behind the boards, look for the next player preparing to receive it. When the broadcast zooms in on a scrum, wait for the wider view before deciding who is open. A surprisingly useful habit is to watch the player who is about to get the puck rather than the player who has it now.

There are several kinds of enjoyment available. You can follow the score, follow a favourite player, appreciate tactical patterns, or care about the long story of a club. You can enjoy a fight scene in Shoresy and still prefer a clean zone exit in an NHL game. You can recognise that a player had a bad night without deciding that he is useless. A team can play well and lose; it can also win while playing a game its coach will dislike.

For your first few Canadiens games, pick three anchors: Nick Suzuki when Montreal has the puck, Lane Hutson when the defence starts an attack, and whichever goalie is actually starting. Add Cole Caufield once following three people becomes easy. The purpose is recognition, not memorisation. Soon you will notice who is on the ice before the commentator tells you.

The guide is a snapshot assembled on 15 October 2026. Roster and statistical tables come from official NHL data. Injury cards carry the date of the report, which may be earlier. Tactical watch points are explanations and questions, not secret knowledge of a coach's instructions. Current-season scores are hidden until you choose to reveal them; the course keeps current-season results out of its chapters. Previous seasons and historical outcomes are discussed openly.
''','During the next game, follow one player for an entire shift. Ask where he goes when he does not have the puck.')

lesson('shape','02 · Six people, one very small puck','Positions, shifts and why everyone keeps getting off.', '''
A normal even-strength lineup has a goalie and five skaters: two defencemen, a centre and two wings. Five-on-five counts the skaters and leaves out the goalies. The names describe starting responsibilities, not fixed patches of ice. A defenceman can lead a rush. A winger may become the last player back. The team still needs somebody to cover the space that has been vacated.

The centre often supports the puck in all three zones, takes many faceoffs and helps the defence down low. Wings offer outlets along the boards, attack the net and help cover the opposing defence near the blue line. Defencemen retrieve pucks, begin breakouts and protect dangerous space in front of their own goal. A goalie does much more than react: he reads passing options, manages depth and communicates with the defence. These are overlapping jobs, not rigid rules.

Teams generally organise their forwards into four lines and their defencemen into three pairs. Those combinations change during games and between games. The first line usually receives substantial attacking opportunity, but a third-line specialist can be essential to winning. A depth player who kills penalties and starts shifts against strong opponents has a different assignment from a winger deployed beside an elite creator.

Hockey is played in short, intense bursts called shifts. A skater may be out for roughly forty to sixty seconds, though circumstances vary enormously. Sprinting, stopping, accelerating and wrestling for position burn energy quickly. Players change during stoppages and on the fly. A sensible chip into the offensive zone can buy time for tired teammates to get off. A spectacular extra rush can become a terrible decision if it leaves an exhausted group trapped defending.

Changing on the fly is a tactical vulnerability. If one player leaves before a replacement can join the play effectively, an opponent may attack the gap. Too many players participating at once can draw a bench penalty. Watch the far side of the rink when a tired team finally gains possession: several players may turn toward the bench immediately. That is often why a pass goes into safe space instead of toward goal.

The home coach normally gets the last line change at eligible stoppages, after seeing the visitors' personnel. That helps create matchups: a checking centre against a dangerous scorer, or an attacking line against a weaker defensive pair. This advantage has exceptions, including restrictions after icing. If a commentator talks about sheltering a player, he usually means choosing easier circumstances or avoiding an especially difficult opponent, not literally keeping him away from contact.

Sweater numbers are recognition tools. For Montreal, fourteen is Suzuki, thirteen is Caufield, twenty is Slafkovsky and forty-eight is Hutson in this snapshot. Do not make every new player a memory test. Learn a line, then a pair, then the people whose shifts keep attracting your attention. A roster listing does not guarantee that somebody will dress tonight.
''','Watch a line change. Was the puck placed somewhere safe first, and did the replacement arrive before the next attack?')

lesson('rink','03 · The rink makes the rules make sense','Offside, icing and the geography of an attack.', '''
Think of the rink as three large regions divided by two blue lines. The zone containing your goal is your defensive zone. The middle is the neutral zone. The zone containing the other goal is your offensive zone. A team attacking toward the other end sees those labels reversed. The red centre line has a different job from the blue lines. The thin red line through the net is the goal line, and play continues behind it because the boards enclose the ice.

Offside is about entering the attacking zone. In the ordinary case, the puck must enter before the attacking players are fully across the blue line. There are detailed skate-position and possession exceptions, so a television replay that looks obvious at full speed may be less obvious in the rulebook. The beginner's question is simple: did an attacker get into the zone too early? When attackers leave and clear the zone during a delayed offside, play can sometimes continue without a whistle.

Why does that rule matter tactically? It prevents a forward from permanently waiting beside the opponent's goalie while the action is at the other end. It also makes the blue line a defensive checkpoint. A defender with good gap control approaches an attacker closely enough to make entry difficult without getting beaten cleanly. An attacking team may carry the puck across, pass it across, or shoot it past that checkpoint and chase it.

Icing is different. Broadly, it involves sending the puck from your side of centre beyond the opponent's goal line without a qualifying touch. NHL hybrid icing uses the officials' judgment about the race, rather than making players crash into the end boards at full speed to settle every call. It is not automatic whenever a puck travels a long way; touches, playable pucks and other exceptions matter. A shorthanded team can normally ice the puck while killing a penalty.

The punishment for icing is chiefly territorial: a faceoff comes back near the offending team's goal, and that team generally cannot change its skaters. Imagine five tired players who have spent a minute defending. Throwing the puck away may create a few seconds of relief but leave the same exhausted group facing another dangerous start. That is why an uncontested pass to a teammate can be better defence than a desperate clearance.

The slot is the dangerous central area in front of the net. The crease is the marked space immediately around the goal. The point is near the attacking blue line, usually associated with defencemen. Below the goal line means behind the net, not underneath the ice. The weak side is the side away from the puck. A weak-side attacker who disappears from a defender's attention can become the most important person in the building.

If a whistle confuses you, ask three questions in order. Did somebody enter too early? Did somebody throw the puck all the way down from too far back? Or did an official signal a foul? You will identify most routine stoppages without mastering the exceptions. For the edge cases, the official video rulebook linked in the library is much better than a confident stranger arguing over one frozen frame.
''','On the next zone entry, decide whether the team carried, passed or dumped the puck in. Notice which option preserved possession.')

lesson('penalties','04 · The power play changes the geometry','Penalties, contact and the difference between toughness and waste.', '''
Physical contact belongs in hockey, but contact is regulated. A legal body check generally targets an opponent eligible to be checked, within limits about timing, location and technique. Having the puck does not make a player fair game for a dangerous hit to the head or a check from behind. Being large does not turn holding, hooking or interference into good defence. The most useful question is not whether a hit looked dramatic; it is what the checker actually did and whether the opponent was eligible for that contact.

A common minor penalty lasts two minutes. When it creates a manpower disadvantage, the other side has a power play. The penalised team is shorthanded and runs a penalty kill. In ordinary five-on-four play, a power-play goal ends a single minor early. Double minors are two segments, and majors work differently: a major does not simply end because a goal is scored. Coincidental penalties, delayed calls and overlapping penalties can make the arithmetic more complicated than one player walking to the box.

Power plays are often about moving the defence before taking the shot. A player high in the zone can distribute to shooting threats on either side. Somebody occupies the space near the goalie's eyes. Another player becomes available between the penalty killers or near the goal line. If all four defenders face the puck on one side, a quick pass to the other side may force the goalie to move across before a shot arrives. The extra player matters because the defence cannot cover every useful space at once.

This is why shouting shoot every time a player touches the puck can miss the point. A shot into an unobstructed, set goalie from a harmless angle may be less dangerous than one more pass. Equally, endless pretty passing without forcing the defenders to respect a shot becomes easy to anticipate. A functioning power play creates believable threats, not just possession. Watch whether the defenders have to turn their bodies and change assignments.

Penalty killers protect the middle, pressure at chosen moments and clear the puck when they can. A forward may attack a poor reception aggressively but retreat when the opponent has clean control. A defenceman may block the pass through the middle instead of chasing the puck carrier. Good killing is coordinated restraint as much as bravery. A failed clearance can be as costly as a failed block, because it gives tired players another thirty seconds of work.

When an official has a delayed penalty pending against the other team, the non-offending side may replace its goalie with another skater because play normally stops when the offending team gains possession. Later in a game, a losing team may pull its goalie voluntarily to attack with six skaters. That is a calculated risk: the empty net makes the next goal easier for the opponent too. Neither situation should be mistaken for a normal power play.

Fighting often results in major penalties for both participants, but the complete set of calls determines whether anyone receives a power play. Shoresy makes the performance of intimidation part of the entertainment. In an NHL game, judge an intimidating player by whether he helps his team retain the puck and avoid dangerous chances. An unnecessary penalty while your best attackers sit down is a measurable cost, however impressive the chirp was.
''','On a power play, follow the player without the puck nearest the crease. Is he screening, redirecting, retrieving, or offering a pass?')

lesson('tactics','05 · Watch the next pass','Breakouts, forechecks and the parts the camera almost misses.', '''
A breakout is the attempt to leave the defensive zone with useful control. It often begins with a defenceman retrieving the puck near the end boards. Before he touches it, the quality of the breakout may already have been decided. Did he look over his shoulder? Did a teammate move into a passing lane? Did the nearest forward come back low enough to help? A pressured player without support can look much worse than the same player receiving good options.

The forecheck is the pressure applied while trying to win the puck back in the opponent's end. The first forechecker may steer the puck carrier toward one side rather than expect to steal it immediately. The next player anticipates the forced pass. A third forward often stays high enough to prevent an easy counterattack. If everybody races below the goal line, the pressure looks enthusiastic but one successful outlet can leave the opponent attacking open ice.

Numbers such as one-two-two or two-one-two describe broad forechecking shapes, not five people permanently standing on dots. The important beginner questions are practical. How many players commit deep? Which passing route is being blocked? Who is responsible if the puck gets past them? Teams can change their pressure according to score, opponent, fatigue and where the puck is. A single clip is rarely enough to label an entire season's system.

Through the neutral zone, speed and spacing become especially visible. A forward crossing with possession may draw a defender inward and open a lane outside. Another attacker may drive toward the net without expecting a pass, forcing a defender to retreat. Defenders want manageable gaps, support through the middle and enough backward speed to avoid a clean breakaway. Standing still at the blue line can look decisive until somebody goes past you.

A dump-in deliberately sends the puck behind the defence. It can be sensible when the blue line is crowded, a line needs to change or the attacking team has a good chance of arriving first. It can also be a cheap surrender when nobody can chase it. Judge the recovery, not the aesthetic preference for carrying the puck. A controlled entry is valuable because it retains possession, but trying to skate through three defenders is not automatically the sophisticated option.

Once established in the offensive zone, cycling means using movement and short exchanges to keep possession and alter defensive coverage. A defenceman who pinches steps down the boards to keep a puck in or pressure a receiver. A forward must often cover behind him. A successful pinch can sustain a dangerous attack. A badly timed one can create an odd-man rush the other way. The same action is a risk with a context, not inherently smart or reckless.

Try watching the weak side. When the puck is on the left boards, look right. Is a winger waiting for a cross-ice pass? Is the far defenceman available? Has a defender lost track of somebody behind him? This habit makes hockey feel slower because you begin to anticipate options. When a commentator praises hockey sense, much of it is this ability to recognise what is about to become available before everybody else gets there.

For Montreal, use Hutson as a practical study in manipulation. Watch his feet and shoulders before looking at the outcome. For Minnesota, compare how Hughes creates room with how Faber provides an outlet. For Pittsburgh, watch Crosby below the circles. For Ottawa, watch Stützle enter with speed. For Seattle, look for the second forechecker who turns an ordinary dump-in into retained possession. These are watching lenses, not guarantees that every shift will follow the same pattern.
''','Ignore the puck for ten seconds and watch the weak-side winger. What option does his position create?')

lesson('goalies','06 · Understanding the goalie without blaming him for everything','Screens, rebounds and why a save percentage needs company.', '''
A goalie is trying to solve a geometry problem while people deliberately obstruct the information. The shooter has an angle, the puck has a path and potential receivers may change that path. The goalie chooses how far from the goal line to stand, how square to the puck to remain and when to commit to a movement. Coming farther out can reduce the visible net, but it also leaves more distance to travel if the puck moves sideways.

The butterfly is the familiar position with the knees down and pads spread to cover low space. It is a tool, not a sign that the goalie has given up standing. Modern goaltending combines controlled movement, tracking and recovery. A quiet save in which the puck hits the chest may reflect excellent positioning. A spectacular desperate save may reflect brilliance after an earlier problem, or a teammate's mistake that left no easy option.

A screen blocks the goalie's view. A deflection changes the puck's direction after the original shot. A rebound gives the attack another chance before everyone can reset. Those are different ways to make an apparently ordinary shot dangerous. Ask whether the goalie could see the release, whether he had to move laterally and whether anybody was allowed an uncontested second attempt. Saying he should have had it is more informative when you explain which of those conditions made the save reasonable to expect.

Rebound control means directing or holding a puck so that it does not become an immediate problem. A save pushed safely into a corner differs from a puck left in the slot. Defencemen help by tying up sticks and clearing the area without screening their own goalie. A goalie can play the puck behind the net to help a breakout, subject to the restricted trapezoid rules. That skill can save a defenceman from taking a heavy hit on a retrieval.

Save percentage is saves divided by shots on goal faced. A value of point nine one zero means ninety-one percent, not nine percent. Goals-against average expresses goals allowed per sixty minutes; it is affected by the defence as well as the goalie. Neither number describes the quality of every chance. Goals saved above expected compares goals allowed with a model's estimate for the shots faced. Different models can disagree because their inputs and assumptions differ.

Goaltending is noisy over short periods. A few screened goals can change a weekly percentage dramatically. A goalie who wins a game is not automatically the goalie who played better. Compare workload, opportunity quality, rebound control and a meaningful number of starts. Health and workload management also matter. A club's goalie depth can become central very quickly when a starter is unavailable.

In Montreal's current roster snapshot, Samuel Montembeault, Jakub Dobeš and Jacob Fowler are the goalie names to learn. An injury card and the actual game lineup tell you more about tonight's starter than the order of those names. Avoid treating a promising young goalie as a finished product after one excellent game or as a failed prospect after one rough one. Development is especially hard to read when the player behind the mask is asked to erase everybody else's mistakes.
''','After the next goal against, identify the shot, the screen, the pass before the shot and any rebound. Then decide what the goalie could reasonably control.')

lesson('season','07 · What a season is actually trying to prove','Standings, the Cup and the difference between one night and a year.', '''
The NHL has thirty-two clubs arranged in two conferences and four divisions. Montreal and Ottawa play in the Atlantic Division. Pittsburgh is in the Metropolitan. Minnesota is in the Central, and Seattle is in the Pacific. The first two divisions belong to the Eastern Conference; the other two belong to the Western Conference. Division neighbours meet often enough to develop familiarity, strategic adaptations and reasons to annoy each other.

The 2026–27 regular season has eighty-four games per team. The previous seasons in this guide had eighty-two. That distinction matters when somebody compares totals without checking the schedule. A player can accumulate more points simply by playing more games, and a team's point total should be read alongside games played. Points percentage asks what share of the maximum available standings points a team has earned.

A win earns two standings points. An overtime or shootout loss earns one. A regulation loss earns zero. In a record written wins, losses, overtime losses, the final number includes shootout losses. A team with forty wins, thirty regulation losses and ten overtime losses has played eighty games and earned ninety points. The arithmetic explains why a club with many overtime defeats can stay close to a club with more wins.

The playoff field has sixteen teams. Under the division and wild-card structure, the top three in each division qualify, plus two wild cards in each conference. A wild card is therefore not a separate division and does not mean the team is bad. Standings ties are resolved using multiple criteria; regulation wins matter before several later tiebreakers. If two clubs are level on points with different games played, do not pretend the standings tell the whole story.

Regular-season overtime is a short three-on-three period followed, if necessary, by a shootout. Playoff overtime uses full-length sudden-death periods at five-on-five until somebody scores. A playoff series is best of seven: four victories advance a team. Winning the Stanley Cup requires winning four series. That format tests depth, health and adaptation differently from an isolated regular-season meeting.

When you see a game called a four-point game, the speaker usually means two rivals are competing for the same place in the standings and the result can create a relative swing. It is not a special scoring rule. Games in hand means one team has played fewer games and therefore has opportunities still to come, not points already banked. Strength of schedule describes the difficulty of opponents and circumstances, which can complicate early comparisons.

For a beginner, use three time scales. One game tells a small story about execution and luck. Ten or twenty games begin to reveal patterns, though injuries and opponents still matter. Several seasons reveal whether the organisation is moving toward its intended window of competitiveness. Montreal improving across the three completed seasons in the tables is more meaningful evidence of progress than a single October result. It still does not entitle the team to win the next game.
''','Read a standings record and calculate the points yourself. Then check games played before comparing two teams.')

lesson('stats','08 · Stats that make you harder to fool','A small toolkit, with the limits attached.', '''
Start with goals, assists and points. A player's points equal goals plus assists. Up to two assists can be awarded on a goal. A second assist may be a brilliant pass that started the whole attack or a relatively ordinary contribution; the box score does not distinguish them. A high point total is evidence of production. It is not a complete description of defending, usage, teammates or opportunity.

Time on ice is context. Twenty minutes in a difficult matchup is a different job from ten minutes of sheltered attacking shifts. Power-play time adds opportunities that some players do not receive. Per-game statistics help compare players who missed games, but a player cannot help his team while absent. Per-sixty-minute rates adjust for playing time; they can also make tiny samples look deceptively impressive. A rate and its sample size belong together.

A shot on goal is a shot that would enter the net without a save. Attempts that miss the target or get blocked are counted differently. Corsi is a name for all shot attempts; Fenwick excludes blocked attempts. Possession discussions often use those attempts as a proxy for which team is spending time attacking. They are not a literal stopwatch of puck control, and an easy outside attempt is not equivalent to a dangerous chance from the slot.

Expected goals assigns a probability to a shot using a model's information about the chance. Adding those probabilities estimates the goals that collection of chances might usually produce. It is useful for separating opportunity creation from finishing in a small sample. It does not say that a team deserved an exact final score, and it does not see everything a coach or viewer can see. Public models vary, so compare like with like and name the provider when making a precise claim.

Plus-minus adds or subtracts for certain goals while a player is on the ice, excluding many power-play situations and with other rule details. It is heavily affected by teammates, goalies and deployment. It is a clue to investigate, not a defensive ranking. A strong player on a weak team can look poor by this measure. A passenger on a dominant line can look excellent.

Shooting percentage is goals divided by shots on goal. A sudden spike can reflect improved chances, exceptional finishing, random variation or some combination. PDO adds a team's on-ice shooting percentage and save percentage, usually on a scale around one thousand. People use it as a warning about unusually favourable or unfavourable percentages. It is not a law requiring every team to return to exactly the same number, because skill and context still exist.

Team power-play percentage measures goals per opportunity, and penalty-kill percentage measures opportunities survived without allowing a power-play goal. Those summary rates hide opportunity length, short-handed goals and changing personnel. A team that draws lots of penalties may benefit more than a slightly more efficient team that rarely gets a power play. Special teams and five-on-five performance should be examined separately before being combined into a full picture.

Here is a useful fan sentence: I like the chances they are creating, but I want a larger sample before deciding the finishing has changed. Another is: the goalie faced difficult lateral plays, so the raw percentage needs context. Those statements leave room to update your opinion. Be suspicious of any stat used as a conversation-ending verdict about a whole player. The point of numbers is to help you ask a sharper question.
''','Pick a leading scorer from a completed season. Compare points, games played and power-play goals before deciding what drove the total.')

lesson('building','09 · How teams become good, and stay stuck','Drafts, contracts, development and the idea of a window.', '''
An NHL club is managing two teams at once: the group playing tonight and the group it hopes to have several years from now. Draft picks bring rights to young players who may need time in junior hockey, college, Europe or the minor leagues. A high selection improves the odds of finding talent; it is not a delivery guarantee. The environment around a prospect, the opportunities he receives and his health can matter as much as the draft-night excitement.

The AHL is the primary professional development league below the NHL. Montreal's affiliate is the Laval Rocket. Minnesota's is the Iowa Wild. Pittsburgh's is Wilkes-Barre/Scranton, Ottawa's is Belleville and Seattle's is the Coachella Valley Firebirds. A player moving between leagues is not automatically being punished. He may need playing time, a different role or room to work on a weakness without being asked to solve an NHL problem immediately.

The salary cap restricts what a club can commit to its roster under a complicated accounting system. A cap hit is not always the same as the actual cheque a player receives that season. A cheap young contributor can create room for expensive veterans. An underperforming long contract can reduce flexibility. Injured reserve and long-term injury relief have specific rules; placing a player on a list does not simply erase all obligations.

A trade can exchange players, draft picks and other rights. Salary may be retained within the rules. A no-trade or no-movement clause can limit what a team can do. Free agents may have restricted or unrestricted status, affecting their freedom and the original team's rights. Contract limits and cap rules changed under the newer agreement, so avoid applying an old eight-year, seven-year slogan to every new deal. Existing agreements and newly signed ones may live under different provisions.

A rebuild means prioritising a stronger future, often by accepting short-term weakness in exchange for prospects, picks or financial flexibility. A retool tries to change the supporting cast while retaining a competitive core. Going all-in means spending future assets or flexibility on a better present chance. Those labels can conceal poor decisions. Ask what the team actually gained, what it gave up and when the acquired players are likely to help.

A championship window is a period when enough talent, development and contract value overlap to make a serious run plausible. Montreal's young core, Pittsburgh's established stars and Seattle's developing centres create very different timelines. Minnesota is trying to combine exceptional skill with enough depth and stability. Ottawa is trying to turn an emerging core into sustained results while absorbing major roster change. These are useful comparison lenses, not predictions or probabilities.

When judging management, distinguish a reasonable decision from a lucky outcome. A sensible move can fail after an unpredictable injury. A reckless move can work briefly because a goalie gets hot. Over time, good organisations need to draft, develop, allocate minutes, handle health and manage contracts consistently. Your best question after a trade is not who won the announcement. It is what problem each side was trying to solve and what new problem it accepted.
''','Choose a young player and ask whether the next useful step is more NHL minutes, a different role, or more development time elsewhere.')

lesson('montreal','10 · Montreal: a club carrying a century','Your team, its history and the weight behind the sweater.', '''
Montreal is an excellent choice if you enjoy caring a completely unreasonable amount about a group of strangers. The Canadiens were founded in 1909, before the NHL itself. Their twenty-four Stanley Cups are a central part of the club's identity. One predates the NHL, so twenty-four Stanley Cups and twenty-four NHL championships are not interchangeable descriptions. The last Cup arrived in 1993. The distance between that date and the present is part of what makes every promising new generation emotionally loaded.

The nickname Habs comes from Les Habitants, a historical term associated with French settlers in Quebec. The H in the crest stands for hockey, not Habitants. The team's identity sits within the history of Quebec, language and Montreal as a city. That context helps explain why a player or coach can carry symbolic significance beyond a stat line. You do not need to adopt somebody else's political interpretation to recognise that the club means more than a sports business to many supporters.

Maurice Richard belongs near the beginning of any account of the Canadiens' mythology. His scoring, intensity and public importance helped make the Rocket an enduring figure. Jean Béliveau represents a different but equally powerful ideal of brilliance and leadership. Five consecutive Cups from 1956 through 1960 established a standard no subsequent NHL team has matched. Later came the four straight championships from 1976 through 1979, with Guy Lafleur's speed and artistry among the defining images.

Goaltending is another thread. Ken Dryden became a central figure in the 1970s. Patrick Roy's rookie-season Cup in 1986 and the 1993 title reinforced the idea that a goalie can become the face of Montreal's biggest moments. Carey Price carried that tradition into a very different era. It is tempting to turn every young Canadiens goalie into the next one of those names. Resist that temptation long enough to let him be his own player.

The Forum was the historic home; the Bell Centre is the current one. Retired numbers and the pregame presentation turn a visit into an encounter with the past. That can be inspiring and burdensome. A young player is not responsible for repairing thirty years of disappointment in one shift. If Montreal gets called a pressure market, that is partly what people mean: performance is discussed in a setting where generations of achievement are permanently present.

The 2021 run to the Stanley Cup Final showed how quickly a season can become a shared memory. Montreal lost to Tampa Bay, but the journey mattered. The years that followed brought a reset and a younger core. The three completed regular seasons in your guide trace a move from seventy-six points to ninety-one and then one hundred and six. Treat the upward line as evidence of change, not an automatic promise of the next step.

Boston is the great recurring historical antagonist. Toronto adds another old and culturally loaded rivalry. Ottawa provides a nearer contemporary Canadian matchup with its own developing story. You do not need to hate everybody on command. Rivalries become meaningful when a game, playoff series or particular player gives you your own reason. Watch a few meetings before borrowing a grievance from somebody who was angry in 1979.

Your simplest Montreal identity card is this: a French-Canadian institution with unmatched Cup history, a long modern wait and an exciting young core. The fun is learning what this particular group becomes. Enjoy the old banners without demanding that every October resemble a dynasty. The crest gives the team a past. Suzuki, Caufield, Hutson, Slafkovsky and their teammates still have to create the present.
''','Pick one historical era to explore next: Richard, the 1970s dynasty, Roy, Price, or the 2021 run.','Canadiens deep dive')

lesson('montreal-people','11 · Montreal: learn these people first','A viewing guide to the core and the jobs around it.', '''
Start with captain Nick Suzuki. A centre's value is easy to underestimate if you watch only the final touch before a goal. Follow Suzuki's support routes, how quickly he makes the next decision and where he positions himself when Montreal loses possession. A centre who makes his wings' jobs easier can affect an entire line without dominating the highlight reel. Number fourteen is your anchor when the game feels too fast.

Cole Caufield wears thirteen. The obvious skill to notice is finishing, but the interesting part often happens before the shot. Watch how he leaves a defender's attention, changes his angle and presents his stick as a target. A smaller scorer cannot simply stand in the same spot and expect the defence to forget him. Timing and deception create the fraction of a second in which a quick release becomes dangerous.

Juraj Slafkovsky, number twenty, brings a different physical shape to the attack. Instead of equating size with hitting, watch puck protection, reach, board work and the ability to continue a play through contact. A big winger helps a skilled line if he turns a contested puck into a controlled pass. He does not need to win every collision in order to be useful. The better question is whether his physical advantages create time for his linemates.

Lane Hutson, number forty-eight, is the defenceman to watch when you want to see a defender make the first mistake without touching him. Look at the small changes of direction, the implied pass and the way he draws pressure. Every offensive defenceman also has to manage the space behind him. When Hutson attacks, look for the teammate covering his position. Evaluating the risk requires seeing that supporting structure as well as the skill.

Noah Dobson, number fifty-three, adds another important right-shot defensive option. Kaiden Guhle, number twenty-one, and Mike Matheson, number eight, are other major names in the defensive picture. Alexandre Carrier and the younger defenders fill different roles according to the lineup. David Reinbacher and Adam Engström are worth tracking as developing defencemen, while Arber Xhekaj is easy to notice because of the physical dimension he can bring. A roster page alone cannot tell you the pairings or minutes for tonight.

Ivan Demidov is a young attacking talent to learn, with creativity as an obvious viewing question. Kirby Dach, Alex Newhook and Oliver Kapanen are useful names when thinking about support through the middle and the distribution of offensive responsibility. Phillip Danault and Jake Evans are worth watching for less spectacular centre work: faceoffs, defensive routes and difficult assignments. Josh Anderson and Chris Kreider give the group experienced physical options. The current roster has changed, so an old guide may still list players who have moved on.

Martin St. Louis is the head coach in this edition. As a player, he reached the Hall of Fame despite being undrafted and undersized by traditional NHL expectations. That background makes development an interesting lens through which to watch his coaching, but a biography does not prove a system works. Judge the team by its spacing, decisions, special teams and whether young players become more complete. Kent Hughes is the general manager, a different role responsible for building the roster rather than choosing every shift.

Finally, learn the difference between a depth chart and a lineup. An injured player may appear on the official roster. A healthy player may be scratched, meaning not selected to dress. A prospect may be recalled for cover and never start. Goalie availability can change the entire evening. The app's injury cards and full roster are dated separately, and neither should be mistaken for a promise about who will be on the ice in a future game.
''','For one period, watch Suzuki before he receives the puck and Caufield before he becomes the shooter.','Canadiens deep dive')

lesson('montreal-watch','12 · Montreal: what better hockey would look like','Strengths, pressure points and a useful game-watching routine.', '''
Here is a way to evaluate Montreal without turning every result into a referendum on the rebuild. Begin with the first pass out of the defensive zone. If the defenceman has to fire the puck blindly up the wall, ask whether the forwards offered support. If Montreal exits under control, watch how many attackers enter the neutral zone together. Connected groups give a skilled puck carrier options. Isolated stars have to beat too many people alone.

The obvious upside of a core containing Suzuki, Caufield, Slafkovsky and Hutson is the possibility of combining different strengths. A centre can organise possession, a finisher can convert it, a large winger can extend it and an inventive defenceman can change the angle of attack. That is an analytical lens based on their roles, not a guarantee of chemistry on every line combination. The supporting cast must still win pucks, offer outlets and keep the middle protected.

One pressure point is what happens after a defender joins the attack. Can a forward cover behind him? Does a lost puck become an ordinary recovery or an uncontested rush against? A second is secondary creation. When an opponent limits the main scoring threats, can another line create a dangerous possession rather than merely survive? A third is discipline. Giving away repeated power plays can undo long stretches of sound five-on-five play.

The completed-season table gives you a starting hypothesis: Montreal's points and scoring improved across the three years shown. To understand whether that improvement can persist, separate finishing, chance creation, defensive suppression and goalie performance. The data here does not include a proprietary expected-goals model, so it would be dishonest to invent a sophisticated model score. Use the actual shots, goals, special-team rates and player production, then add what you observe.

Injury history is part of this story, but history and present status are different fields. Kirby Dach suffered a season-ending right-knee ligament injury in 2023. Cole Caufield's 2022–23 season ended for shoulder surgery. Those facts explain interruptions in development and why supporters pay attention to availability. They do not prove either player is currently injured. A day-to-day label is not a reliable return date, and a roster listing is not medical clearance.

The current Montreal injury card cites the 14 October report. It lists several absences or concerns and deliberately avoids predicting recovery. If a key forward is missing, the interesting tactical consequence is how the remaining centres and wings are deployed. If a puck-moving defenceman is missing, the team may have fewer clean exits. If a goalie is out, workload and the backup plan matter. Those are consequences to watch, not diagnoses to make.

Use a three-part game routine. Before puck drop, check the actual starting goalie and line combinations. During the first period, watch exits and entries without judging the whole game yet. In the second, follow one supporting line and one defensive pair. In the third, notice how the coach changes risk according to the score. Afterward, write one thing the team did well, one recurring problem and one uncertainty. You will learn faster than by collecting hot takes.

Your best Canadiens conversation starter is: I am watching whether their skill stays connected when the opponent takes away the first option. That question works after a win and after a loss. It invites evidence rather than asking your friends to accept a verdict. Over time, you will have your own favourite player, your own recurring complaint and your own memories. That is the point at which a team picked on vibes becomes your team.
''','After a game, record one repeatable strength, one recurring weakness and one question you cannot answer yet.','Canadiens deep dive')

lesson('wild','13 · Minnesota: skill in the State of Hockey','The gang’s Wild guide.', '''
Minnesota calls itself the State of Hockey for reasons that run through youth, school, college and professional life. The Wild joined the NHL in 2000. They are not the same franchise as the Minnesota North Stars, who moved to Dallas in 1993. That distinction matters because the Wild inherited a passionate hockey environment, not the North Stars' record book. The club's identity includes both a strong local tradition and the frustration of trying to turn regular relevance into a deeper championship story.

The early Wild reached the Western Conference Final in 2003 under Jacques Lemaire. Marián Gáborík supplied a star attacking identity, and Mikko Koivu later became a defining captain. The 2012 arrivals of Zach Parise and Ryan Suter signalled ambition; their later buyouts made cap flexibility part of the conversation for years. Kirill Kaprizov's arrival gave the modern club a different kind of attacking focal point. History explains the emotional setting, but it should not trap the current team inside a permanent stereotype about defensive hockey.

Kaprizov, number ninety-seven, is the first person to learn. Watch what happens when he changes speed and how defenders react even before he receives the puck. Matt Boldy, number twelve, is another major attacking name. Joel Eriksson Ek is an important centre to follow around the net and in difficult matchups. A scorer's job is easier when a teammate occupies defenders, wins a contested puck or forces the goalie to look around a body.

The defence in this snapshot includes Quinn Hughes, Brock Faber, Jared Spurgeon and Jonas Brodin. If you last read about Minnesota before the major changes, that Hughes listing may surprise you; it is present in the current official roster. Watch how a puck-moving defenceman creates an exit, then how his partner provides a safe second option. A pair's value is often the interaction between its members rather than two isolated reputations.

John Hynes is the coach. Other current roster names worth recognising include Ryan Hartman, Marcus and Nick Foligno, Blake Coleman, Danila Yurov and Bobby Brink. The goalie list includes Filip Gustavsson, Jesper Wallstedt and Calvin Pickard. Do not use a familiar retired goalie or an old roster graphic as a substitute for checking the current lineup. Minnesota, like every club here, has changed substantially around its core.

The three completed seasons show eighty-seven, ninety-seven and one hundred and four points. The latest of those seasons reached the second playoff round. A useful next-step question is whether the club can get enough secondary contribution when opponents concentrate on its most dangerous threats. Another is whether special-team execution helps or wastes the skill advantage. The goalkeeping picture deserves careful attention whenever availability changes the distribution of starts.

For your friend's team, the appealing story is that an organisation with deep hockey roots has some genuinely exciting modern attacking talent. The uncertainty is how much of a complete playoff team surrounds that talent. Look for support through the middle, clean exits under pressure and whether depth forwards generate useful shifts against good opponents. Do not reduce the Wild to Kaprizov and four anonymous helpers. Equally, do not assume recognisable names automatically create a balanced roster.

A friendly question for the Wild supporter: when the top threats are tightly covered, who makes the next useful play? That moves the conversation beyond whether the star scored. For a Canadiens fan, Minnesota is also a good comparison for learning how a creative defenceman changes the rhythm of an entire attack. Follow the puck out of the defensive end, and you will see the connection between skill at the back and danger at the front.
''','Compare one Hughes breakout with one Hutson breakout. Which passing options did their teammates provide?','The gang’s teams')

lesson('penguins','14 · Pittsburgh: living legends and the next chapter','The gang’s Penguins guide.', '''
Pittsburgh joined the NHL in 1967. Its history is unusually tied to a succession of extraordinary players. Mario Lemieux arrived through the 1984 draft, became a transformative star and later helped preserve the organisation through an ownership role. The 1991 and 1992 Cups, with Jaromír Jágr among the central figures, created one great era. Sidney Crosby's arrival in 2005 helped begin another. The Penguins won again in 2009, 2016 and 2017, bringing the total to five Cups.

That history creates a particular emotional bargain for the present. Fans are still watching players who belong in an all-time conversation, while the organisation must also plan for life after them. Calling it a rebuild can miss the competitive ability of the veterans. Calling it one last ride every year can miss the work of developing the next group. The tension between honouring a remarkable core and creating a sustainable future is the central viewing story.

Start with captain Sidney Crosby, number eighty-seven. Watch below the faceoff dots and along the boards, not just when a goal appears likely. Notice how his body separates a defender from the puck, how quickly he can change the passing angle and how a short touch creates a better position for the next player. A signature backhand or deflection is memorable, but the accumulated small advantages are what make following him instructive.

Evgeni Malkin, number seventy-one, provides another kind of attacking presence. Kris Letang, fifty-eight, remains a major name on defence, and Erik Karlsson, sixty-five, is another prominent puck-moving defenceman. Bryan Rust and Rickard Rakell are established names to recognise around the forwards. The younger group includes Ben Kindel and Ville Koivunen. The goalie roster lists Arturs Šilovs and Sergei Murashov in this edition, which is one reason an old guide is a poor way to identify the current crease.

Dan Muse is the coach in this snapshot. A useful coaching question is how the team distributes difficult assignments and manages the interaction between veteran skill and younger legs. An ageing roster is not automatically slow in every situation, and a young roster is not automatically well positioned. Watch recovery after turnovers, support on breakouts and whether the team can maintain its structure late in a long defensive shift.

The completed-season points totals are eighty-eight, eighty and ninety-eight. The last of those seasons returned Pittsburgh to the playoffs before a first-round exit. The rise is real in the official table; it does not tell you by itself which parts are sustainable. Separate the established stars' production, supporting contributions, special teams and goaltending. Avoid projecting one veteran's entire season from a single excellent week or a few tired shifts.

Pittsburgh's familiar rivals include the Philadelphia Flyers and Washington Capitals. The Philadelphia rivalry has a geographical and divisional edge. The Capitals rivalry gained another layer through Crosby and Alex Ovechkin. Rivalries change shape as rosters change, but an ordinary-looking regular-season date can still carry years of emotional baggage. That is useful context when the crowd reacts as if a Tuesday game is a moral referendum.

For the Penguins supporter in your group, the best question is: how do they keep benefiting from extraordinary experience without asking the same people to solve every problem? Watch a young player's shift immediately after a star line. Does the team sustain the pressure or spend the next minute retreating? For you as a Canadiens fan, Pittsburgh offers a glimpse of what it means when a core becomes an era. Montreal's young players are still writing their first chapters; Pittsburgh's legends already have a shelf.
''','Follow Crosby for one shift without counting points. Find one useful action the box score will not record.','The gang’s teams')

lesson('senators','15 · Ottawa: a changed core with something to prove','The gang’s Senators guide.', '''
The modern Ottawa Senators began play in 1992. The name recalls an earlier championship club, but those early Stanley Cups do not belong to the modern franchise's NHL record. That is similar to the distinction between Seattle's Metropolitans history and the Kraken, or Minnesota's North Stars and the Wild. A city can inherit a hockey memory without inheriting a franchise's statistical identity.

Daniel Alfredsson became a defining modern Senator. The club's long rise included a 2007 trip to the Stanley Cup Final, where Anaheim won. Erik Karlsson later made the defence itself an attacking attraction. In 2017, Ottawa came within a double-overtime Game Seven of another Final. The opponent was Pittsburgh. That is a useful piece of history for your group because one friend's glorious memory can be another friend's lingering ache.

An important current correction comes before any player guide: Brady Tkachuk is not on Ottawa's present roster. Thomas Chabot was named captain in September 2026 after Tkachuk's departure. Older primers often organise the entire Senators identity around Tkachuk, so they will send you into this season with a misleading mental picture. The official roster and captain announcement linked in the app are the reference points for this edition.

Tim Stützle, number eighteen, is the forward to follow first. Watch acceleration through the neutral zone and how defenders respond when he threatens to carry possession inside. Drake Batherson offers another important attacking presence. Dylan Cozens and Shane Pinto are useful centres to learn, while Claude Giroux brings extensive experience. Ridly Greig can draw attention in the difficult, contested parts of a game. William Eklund is another name in the roster snapshot, with availability treated separately in the injury notes.

On defence, start with Chabot and Jake Sanderson. Watch which player retrieves, who supports and how quickly the puck reaches a forward in motion. Jordan Spence, Tyler Kleven and Carter Yakemchuk are other current names worth recognising. Linus Ullmark and Samuel Ersson are the goalies listed. Travis Green is the head coach. Again, learning those names gives you bearings; it does not settle the night's pairings, starter or assignments.

The completed-season table rises from seventy-eight points to ninety-seven and ninety-nine. Those totals describe a team that became more competitive, but the playoff column is a separate test. To understand the next step, ask whether the club can create enough chances against organised opponents and protect the middle without depending on a goalie to erase repeated breakdowns. Roster change also makes assumptions about old line chemistry less useful.

Ottawa's Battle of Ontario with Toronto is the rivalry label to know. Montreal is a nearby Canadian opponent with its own reasons for emotional games. Compared with the Canadiens' enormous historical weight, modern Senators fandom has a younger narrative: building legitimacy, remembering near misses and trying to turn an appealing core into something durable. A fan may be optimistic and deeply suspicious at exactly the same time.

Ask your Senators friend: what changed in the team's identity after the leadership change, and can you see it in the way they play? That is an invitation to watch rather than an assertion that a new captain magically fixes anything. For your own learning, compare Stützle's entries with Suzuki's supporting decisions. There are many ways for a centre to make teammates better, and seeing two different approaches will teach you more than ranking them after one game.
''','Watch whether Ottawa enters the zone with multiple passing options or asks the first puck carrier to do everything.','The gang’s teams')

lesson('kraken','16 · Seattle: becoming somebody','The gang’s Kraken guide.', '''
Seattle's Kraken began NHL play in 2021. The city's hockey history reaches much further back: the Seattle Metropolitans won the Stanley Cup in 1917. They were a different club, so that trophy is historical context rather than a Kraken championship. The distinction lets you appreciate the city's past while recognising that the current fan base is watching a new organisation form its own traditions.

The Kraken's first playoff run in 2023 made an immediate contribution to that identity. Seattle eliminated defending champion Colorado before losing to Dallas in the second round. On New Year's Day 2024, an outdoor Winter Classic at the baseball stadium supplied another memorable image, with Joey Daccord shutting out Vegas. A new club has fewer old banners, but it can acquire meaningful memories surprisingly quickly.

The sea-monster name, blue palette and Climate Pledge Arena give Seattle a different visual and cultural setting from Montreal. The mascot is Buoy, a troll. You do not need a century of grievance to become attached. One attraction of following a newer team is that the foundational players, rituals and rivalries are still being chosen through experience rather than inherited fully formed.

Learn Matty Beniers first. Shane Wright and Berkly Catton are other young centres to track. Watch development as a set of skills rather than a countdown to stardom: support routes, decisions under pressure, defensive responsibility and the ability to make the next play at NHL speed. Jordan Eberle is the captain and an experienced attacking reference point. Jared McCann and Chandler Stephenson are other important names. The current roster also includes Kaapo Kakko, Bobby McMann and Mackie Samoskevich.

Vince Dunn, Brandon Montour and Adam Larsson are key defensive names to recognise, with Ryker Evans another player worth tracking. Joey Daccord and Philipp Grubauer appear in the goalie list. Lane Lambert is the head coach in this edition. A useful way to watch Seattle is to follow the support after the first forechecker. An organised recovery can turn a routine dump-in into sustained pressure; an unsupported chase can give the opponent an easy exit.

The recent completed seasons produced eighty-one, seventy-six and seventy-nine points. Those totals make it reasonable to ask where more repeatable offence can come from. A broad contribution from several lines is helpful, but depth alone is not the same as a top-end chance creator who forces the opponent to reorganise. The question for the young centres is how much attacking responsibility they can earn while remaining dependable without the puck.

The defensive side matters too. Watch whether pressure in the offensive end is backed by a responsible third forward, whether the defence receives help on retrievals and whether the goalie sees the first shot. A team can look busy while conceding the more dangerous opportunities. If Seattle spends an entire shift cycling along the outside, wait to see whether anybody reaches the middle before calling it dominance.

Your Kraken friend has the pleasure and occasional discomfort of helping decide what the club means. Ask which young player has changed most in the small details, and which line can create a chance when the game gets tight. For a Canadiens fan, Seattle is a useful contrast: one club is trying to live up to a huge inherited story; the other is trying to build a lasting one. Both projects become much more interesting when you know the people doing the work.
''','Follow one young Seattle centre through a defensive shift and an attacking shift. Which responsibilities look settled, and which still look difficult?','The gang’s teams')

lesson('culture','17 · Letterkenny, Shoresy and the actual game','Chirps, rituals and how to talk hockey without pretending.', '''
Letterkenny and Shoresy offer a useful emotional introduction: the speed of the language, the dressing-room hierarchy, pride in the group and the theatrical absurdity of chirping. They are comedies with a particular hockey setting, not a complete manual for professional behaviour. An NHL team is also a workplace full of specialists, video meetings, travel, health management and decisions that have nothing to do with winning an exchange of insults.

A chirp is a verbal jab, often delivered as if its speaker has been rehearsing it since childhood. A celly is a celebration. Wheels means skating speed. Hands means puck skill. A beauty can mean an admired player or person; a bender is a mocking term for an unskilled skater. A flow is hair, not an analytical description of neutral-zone transition. You can enjoy the vocabulary without forcing it into every sentence you say.

The code is a loosely used phrase about unwritten expectations. Different players and generations disagree about it. It is not a second rulebook that legalises a dangerous act. Protecting a teammate, answering a challenge and avoiding reckless contact can all be discussed without assuming that the loudest traditionalist has the final word. A big legal hit and an illegal cheap shot are not the same because both make good television.

Captains and alternate captains have formal roles in communication with officials under the rules, alongside informal leadership responsibilities. Wearing a letter does not mean somebody is the team's only leader or necessarily its most talented player. A quiet veteran, a thoughtful goalie or an energetic depth forward can matter to the room. Be cautious when people claim to know the atmosphere inside a team from one bench camera shot.

The sweaters, goal songs, local broadcasts and pregame routines make fandom feel specific. Montreal's language and history differ from Minnesota's grassroots hockey environment, Pittsburgh's long association with transcendent stars, Ottawa's near misses and Seattle's newer traditions. Your group does not need to rank those identities. Let each person explain what makes the team enjoyable to follow, even if the honest answer still begins with the logo.

Here is a useful set of conversation starters. Who makes your favourite scorer's life easier? Which defender do you trust to start a breakout under pressure? What changes when the coach goes to the second power-play unit? Is the problem that the team cannot create chances, or that good chances are not going in? Which young player is getting a harder assignment than last month? Those questions work without a bank of historical trivia.

Friendly banter is better when the information is right. Do not tease Ottawa about its current captain using an old roster, or describe a retired Wild goalie as tonight's starter. Do not use injuries as evidence that a player lacks character. A player missing a game is a person dealing with a health problem, and an upper-body label rarely tells supporters enough to evaluate it. The app links reports precisely so speculation does not become a pretend fact.

Most of all, allow your opinion to develop. You can say that you do not yet understand a call. You can like a player before you can explain every detail of his value. You can disagree with a friend and then watch the next game together to test the idea. A team chosen on vibes is a beginning, not something you need to outgrow. Knowledge gives the feeling more places to attach.
''','Ask each friend for one player to watch away from the puck and one piece of team history that still matters to them.')

lesson('game-night','18 · Your first proper game night','A practical routine and a final set of questions.', '''
Before the game, take two minutes to check the actual lineup and starting goalie. A roster is the list of eligible people in the organisation's current picture; a lineup is the group selected for this game. Notice significant absences, but do not infer medical details. If you are watching a replay, avoid the team news feed until afterward because even an injury article can reveal the result in its surrounding headlines.

In the first five minutes, orient yourself. Which way is Montreal attacking? Who is wearing fourteen, thirteen and forty-eight? Are the lines changing cleanly? Do not force an immediate verdict. One bad bounce or strong shift is a moment, not a season. Let the game establish its rhythm and give yourself one small assignment, such as watching the first pass out of the defensive zone.

At the first power play, identify the extra passing option. Follow the player near the crease and the player waiting on the weak side. Does the puck movement make the penalty killers move, or do the same harmless passes repeat? When Montreal kills a penalty, watch whether it clears the puck safely and earns a change. Surviving a full two minutes with the same exhausted group is a different performance from repeatedly breaking up entries.

During an intermission, glance at the shots but do not let them overrule everything you saw. Ask where the shots came from and whether the goalies could see them. If one team had several power plays, the overall shot total needs that context. If Montreal is ahead, notice whether it keeps attacking sensibly or gives up every possession to protect the lead. Playing safely can mean controlling the puck rather than hiding from it.

In the final period, follow the changes in risk. A trailing team may pinch more aggressively, shorten its bench or pull its goalie. A leading team may seek clean changes and avoid passes that leave nobody covering. Those decisions can be sensible even when a particular attempt fails. Evaluate the available choices, not just the fact that the puck eventually ended up in a net.

Afterward, use a three-sentence notebook. First: this was the repeatable thing I liked. Second: this was the problem I saw more than once. Third: this is what I want to check next game. For example, I liked the low support on the breakout; the weak-side winger kept getting lost during long defensive shifts; I want to see whether that happens with a different pair on the ice. That is already a more useful conversation than declaring the team either fixed or doomed.

As you watch more, add one layer at a time. Learn the third-line centre. Compare home and road matchups. Read a completed-season stat table beside the roster changes. Ask whether an injury altered a role rather than simply removing a name. You do not need to graduate from enjoyment into permanent analysis. The purpose of understanding the game is to make watching it richer.

You are now equipped to follow the broad shape of a game, recognise the central people on five clubs and ask questions that have real answers. The rest comes from accumulated evenings: the unexpected save, the irritating rivalry game, the prospect who suddenly looks comfortable and the goal you will remember because you watched it with your friends. Enjoy the course, and enjoy having a team.
''','Use the notebook after your next Canadiens replay; one observation per field is enough.')

NHL='https://www.nhl.com'
teams=[]
def team(abbr,name,short,city,color,division,coach,captain,identity,hook,history,keys,strengths,questions,recaps,injuries,injury_source,injury_date,extra_sources):
    raw=load(abbr+'-roster.json')
    roster=[]
    for group in ('forwards','defensemen','goalies'):
        for p in raw[group]:
            pname=p['firstName']['default']+' '+p['lastName']['default']
            roster.append(dict(id=p['id'],name=pname,number=p['sweaterNumber'],position=p['positionCode'],hand=p['shootsCatches'],born=p['birthDate'],country=p['birthCountry'],height=p['heightInCentimeters'],weight=p['weightInKilograms']))
    stats={str(y):load(f'{abbr}-{y}.json') for y in (2023,2024,2025)}
    summary=sorted([s for s in load('team-seasons.json')['data'] if s['teamId']=={'MTL':8,'MIN':30,'PIT':5,'OTT':9,'SEA':55}[abbr]],key=lambda s:s['seasonId'])
    current=next(s for s in load('standings-now.json')['standings'] if s['teamAbbrev']['default']==abbr)
    teams.append(dict(abbr=abbr,name=name,short=short,city=city,color=color,division=division,coach=coach,captain=captain,identity=identity,hook=hook,history=history,keys=keys,strengths=strengths,questions=questions,recaps=recaps,injuries=injuries,injurySource=injury_source,injuryDate=injury_date,sources=extra_sources,roster=roster,stats=stats,seasons=summary,current=current,currentStats=load(abbr+'-stats.json'),schedule=load(abbr+'-schedule.json')['games']))

team('MTL','Montréal Canadiens','Canadiens','Montréal, Québec','#ac1833','Atlantic','Martin St. Louis','Nick Suzuki',
 'A century of expectations. A core writing its own story.',
 'Your club. Start with the people, then learn to see the patterns behind the highlights.',
 [['1909','Before the NHL','The Canadiens are founded. The club is older than the league that now contains it.'],['1916','First Stanley Cup','Montreal wins its first Cup before the NHL begins play in 1917.'],['1944–60','Richard and a dynasty','Maurice Richard becomes a defining figure; the club wins five consecutive Cups from 1956 to 1960.'],['1976–79','Four more in a row','The Lafleur-era Canadiens establish another dynasty.'],['1986 & 1993','Roy’s era','Patrick Roy is central to two titles. 1993 remains the latest of Montreal’s 24 Cups.'],['2021','A surprise Final','Montreal reaches the Cup Final and loses to Tampa Bay.'],['2022 onward','A new core','Suzuki, Caufield, Slafkovsky and Hutson become central reference points for the next era.']],
 [['Nick Suzuki','14 · C · Captain','Follow his support below the puck and his next-pass decisions. A centre’s influence extends beyond his own shots.'],['Cole Caufield','13 · R · Finisher','Watch the movement before the release: changes of angle, timing and the passing lane he presents.'],['Juraj Slafkovsky','20 · L · Puck protection','Look for board recoveries and possession extended through contact, rather than counting big hits.'],['Lane Hutson','48 · D · Creator','Watch how small changes of direction make a defender commit. Then check who covers behind him.'],['Ivan Demidov','93 · R · Young creator','Track imagination, decision speed and how opportunities change with availability.'],['Noah Dobson','53 · D · Right-shot option','Watch exits, blue-line decisions and the balance between joining an attack and protecting the next rush.'],['Kaiden Guhle / Mike Matheson','21 / 8 · D','Compare defensive routes and puck-moving responsibilities; availability matters to the pairings.'],['Dobeš / Fowler / Montembeault','75 / 32 / 35 · G','Check tonight’s starter. A full roster can contain unavailable players.'],['Danault / Evans / Dach / Newhook','Centres and support','Learn who takes difficult starts, supports the breakout and creates secondary offence.']],
 ['Complementary attacking roles: a distributor, finisher, puck protector and creative defencemen give you several different things to watch.','The completed-season table shows substantial growth in points and scoring. Check the underlying context before projecting the same rate forward.','There are multiple young players whose development can change the team’s ceiling; a roster is a process rather than a finished diagram.'],
 ['Can the forwards cover when a defenceman activates?','Does a second line create real danger when the top threats are contained?','Are exits connected through the middle, or does every recovery become a clearance?','Do discipline and goalie availability support the attacking talent?'],
 ['2023–24: a development year, 76 points and no playoffs. Use it as a baseline rather than a blueprint for the current roster.','2024–25: 91 points and a return to the playoffs; a first-round loss to Washington.','2025–26: 106 points and a run to the Eastern Conference Final. Regular-season leaders and full historical roster stats appear below.'],
 [['Samuel Montembeault','Lower body','Listed injured; no return date asserted here.'],['Ivan Demidov','Lower body','Listed injured.'],['Oliver Kapanen','Lower body','Listed injured.'],['Florian Xhekaj','Undisclosed','Listed injured.'],['Mike Matheson','Lower body','Day to day in the cited report.'],['History · Kirby Dach','2023 right-knee ACL/MCL injury','Season-ending event in 2023–24. Historical context, not a statement that he is injured now.'],['History · Cole Caufield','2023 shoulder surgery','His 2022–23 season ended early. Historical context, not current status.']],
 NHL+'/news/montreal-canadiens-washington-capitals-game-preview-october-14-2026','14 Oct 2026',
 [['Club history & honours','https://records.nhl.com/mtl/awards/team'],['Dach injury history',NHL+'/canadiens/news/kirby-dach-to-miss-the-remainder-of-the-season'],['Caufield injury history',NHL+'/news/montreal-canadiens-cole-caufield-injury-status-out-for-season-340238372'],['2025–26 season retrospective',NHL+'/canadiens/news/the-2025-26-canadiens-season-one-for-the-books']])

team('MIN','Minnesota Wild','Wild','Saint Paul, Minnesota','#17523e','Central','John Hynes','Jared Spurgeon',
 'A hockey heartland, with artists at the sharp end.',
 'Watch the connection between elite puck movement and the people who turn it into sustained pressure.',
 [['1993','An important distinction','The North Stars leave for Dallas. They are a different franchise.'],['2000','The Wild begin','An expansion club brings NHL hockey back to Minnesota.'],['2003','An early deep run','The Wild reach the Western Conference Final under Jacques Lemaire.'],['2012','A statement of ambition','Zach Parise and Ryan Suter arrive; their later buyouts shape years of cap conversation.'],['2021','Kaprizov arrives','Kirill Kaprizov wins the Calder Trophy and becomes a modern focal point.'],['2025–26','A second-round appearance','A playoff series win creates a new recent benchmark.']],
 [['Kirill Kaprizov','97 · L','Follow the changes of speed and the defensive attention he creates.'],['Matt Boldy','12 · L','A major attacking name; look for how he combines with support through the middle.'],['Joel Eriksson Ek','14 · C','Watch work around the net and the difficult centre responsibilities.'],['Quinn Hughes','43 · D','Yes, on the current Wild roster. Track how the first move changes the breakout.'],['Brock Faber','7 · D','Look at outlets, positioning and his relationship with his partner.'],['Jared Spurgeon / Jonas Brodin','46 / 25 · D','Experienced defensive reference points.'],['Wallstedt / Gustavsson / Pickard','30 / 32 / 31 · G','Availability and workload can alter the entire goalie picture.'],['Danila Yurov / Bobby Brink','22 / 10 · F','Watch how younger supporting players turn skill into dependable shifts.']],
 ['High-end attacking and puck-moving names make the first pass and the second chance especially interesting to watch.','The three completed seasons show a rise from 87 to 104 points.','Different forward roles can complement the stars if the supporting shifts retain possession.'],
 ['Who creates the next useful play when Kaprizov is tightly covered?','Does the penalty kill support the five-on-five work?','How does goalie availability change the workload?','Can the club’s depth sustain pressure against strong opponents?'],
 ['2023–24: 87 points and a missed postseason.','2024–25: 97 points, followed by a first-round exit against Vegas.','2025–26: 104 points and a second-round playoff appearance.'],
 [['Filip Gustavsson','Hip surgery · preseason report','Reported unavailable in the 19 September preview. This older report is not confirmation of his status on 15 October.'],['Coverage note','Latest status not fully established','Check the official team news for a game-day update. An unlisted injury is not evidence of full health.']],
 NHL+'/news/minnesota-wild-season-preview-2026-27','19 Sep 2026 · older report',
 [['Wild official news',NHL+'/wild/news/'],['Wild franchise record','https://records.nhl.com/min/overview/season-by-season-record']])

team('PIT','Pittsburgh Penguins','Penguins','Pittsburgh, Pennsylvania','#bc900c','Metropolitan','Dan Muse','Sidney Crosby',
 'Living legends. An unfinished next chapter.',
 'The challenge is keeping extraordinary experience useful while building the team that follows it.',
 [['1967','Expansion beginnings','Pittsburgh joins the NHL in the league’s first major expansion.'],['1984','Lemieux arrives','The draft brings the player who transforms the franchise.'],['1991–92','First two Cups','Lemieux and Jágr define a championship era.'],['1999','Lemieux the owner','A central player in the club’s history takes on an ownership role.'],['2005–09','The Crosby era begins','Crosby arrives in 2005; a new core wins the 2009 Cup.'],['2016–17','Back-to-back champions','Two more Cups bring Pittsburgh’s total to five.']],
 [['Sidney Crosby','87 · C · Captain','Watch puck protection and short touches below the circles, not only the final shot.'],['Evgeni Malkin','71 · C','A different attacking presence within the veteran core.'],['Kris Letang','58 · D','An established defensive and transition reference point.'],['Erik Karlsson','65 · D','Track the relationship between attacking ambition and protection behind the puck.'],['Bryan Rust / Rickard Rakell','17 / 67 · R','Recognisable attacking support around the core.'],['Ben Kindel / Ville Koivunen','81 / 41 · F','Useful young-player development stories.'],['Arturs Šilovs / Sergei Murashov','37 / 1 · G','The current goalie roster, distinct from older Penguins primers.']],
 ['A veteran core offers exceptional experience and several different forms of attacking skill.','The 2025–26 points rebound provides a concrete recent comparison with the two preceding seasons.','Young supporting players provide a way to judge succession through actual roles rather than slogans.'],
 ['Can younger lines sustain useful shifts after the star line leaves?','How well does the team recover when a risky attacking play fails?','Are veteran minutes distributed in a way the team can sustain?','Do special teams and goaltending reinforce the core’s production?'],
 ['2023–24: 88 points and a narrow miss of the playoff field.','2024–25: 80 points and another missed postseason.','2025–26: 98 points and a playoff return, ending against Philadelphia in round one.'],
 [['Bryan Rust','Returned 7 October','Activated after an upper-body absence. Do not carry an opening-night injury label forward as if it remains current.'],['Coverage note','Other current availability not fully established','Opening-night injured-reserve lists are not a verified 15 October list. Consult the game-day report.']],
 NHL+'/news/nhl-status-report-news-and-notes-october-7-2026','7–8 Oct 2026',
 [['Penguins official news',NHL+'/penguins/news/'],['Franchise season records',NHL+'/penguins/team/season-by-season-record']])

team('OTT','Ottawa Senators','Senators','Ottawa, Ontario','#bd2635','Atlantic','Travis Green','Thomas Chabot',
 'A new leadership chapter, with a core to develop.',
 'Start with the current roster: an old Tkachuk-centred primer will give you the wrong picture.',
 [['1992','The modern Senators','A new franchise revives the name of an older Ottawa club. The old titles are separate.'],['1990s–2000s','Alfredsson’s era','Daniel Alfredsson becomes a defining modern captain.'],['2007','A Cup Final','Ottawa reaches the Final and loses to Anaheim.'],['2017','One goal short','A double-overtime Game Seven loss to Pittsburgh ends the conference-final run.'],['2023','Ownership changes','Michael Andlauer’s ownership era begins.'],['2026','A new captain','Thomas Chabot becomes captain following Brady Tkachuk’s departure.']],
 [['Tim Stützle','18 · C','Watch acceleration, controlled entries and how defenders react to his approach.'],['Drake Batherson','19 · R','An important attacking partner to recognise.'],['Thomas Chabot','72 · D · Captain','Follow the first pass and the support available on retrievals.'],['Jake Sanderson','85 · D','Watch positioning and the transition from defending to attacking.'],['Dylan Cozens / Shane Pinto','24 / 12 · C','Centres to follow as the team distributes responsibilities.'],['Claude Giroux / Ridly Greig','28 / 71 · F','Different kinds of experience and contested-puck work.'],['Linus Ullmark / Samuel Ersson','35 / 30 · G','Check the actual starter and current availability.'],['William Eklund','27 · L','Listed in the current roster; see the separately dated availability note.']],
 ['Recent points totals establish a much stronger baseline than 2023–24.','There are multiple centres and attacking names to study, rather than a single-player story.','A leadership change makes the formation of a new identity an interesting question.'],
 ['Can the attack create chances against a settled defence?','Does support arrive quickly enough for controlled exits?','How is responsibility redistributed after major roster changes?','Can the team protect the middle without relying on repeated goalie rescues?'],
 ['2023–24: 78 points and a missed postseason.','2024–25: 97 points, then a first-round loss to Toronto.','2025–26: 99 points; Carolina eliminates Ottawa in the first round.'],
 [['William Eklund','Ankle','Reported absent in the 10 October lineup.'],['Jake Sanderson','Undisclosed','Listed injured on 10 October; not a verified 15 October status.'],['Artem Zub','Knee','Listed injured in the same report.'],['Kurtis MacDermid','Upper body','Listed injured in the same report.'],['Cameron Crotty','Illness / IR move','Placed on injured reserve in the 11 October team report.']],
 NHL+'/predators/news/nashville-predators-ottawa-senators-game-preview-october-10-2026','10–11 Oct 2026',
 [['Chabot named captain',NHL+'/senators/news/ottawa-senators-name-thomas-chabot-as-11th-captain-in-franchise-history'],['11 October roster move',NHL+'/senators/news/jorian-donovan-recalled-from-belleville-for-the-second-time'],['Senators official news',NHL+'/senators/news/']])

team('SEA','Seattle Kraken','Kraken','Seattle, Washington','#247e8b','Pacific','Lane Lambert','Jordan Eberle',
 'A young club making its own mythology.',
 'Follow the centres, the second forechecker and the search for repeatable offence.',
 [['1917','Seattle’s earlier Cup','The Metropolitans win the Stanley Cup. They are not the Kraken franchise.'],['2021','The Kraken begin','An expansion club joins the NHL.'],['2023','A first playoff chapter','Seattle beats defending champion Colorado, then loses to Dallas in round two.'],['2024','An outdoor memory','Joey Daccord shuts out Vegas at Seattle’s Winter Classic.'],['2024 onward','A developing core','The club works to build a durable identity around young players and established support.']],
 [['Matty Beniers','10 · C','A young centre to follow in both directions, especially decisions under pressure.'],['Shane Wright / Berkly Catton','51 / 27 · C','Track responsibility and progress, rather than demanding instant stardom.'],['Jordan Eberle','7 · R · Captain','An experienced reference point in a young club’s story.'],['Jared McCann / Chandler Stephenson','19 / 9 · F','Important names around the attack.'],['Vince Dunn / Brandon Montour','29 / 62 · D','Watch the first pass and the decision to join the rush.'],['Adam Larsson / Ryker Evans','6 / 41 · D','Compare defensive responsibilities and support on retrievals.'],['Joey Daccord / Philipp Grubauer','35 / 31 · G','The two goalie names in the roster snapshot.'],['Bobby McMann / Mackie Samoskevich','74 / 11 · F','Current supporting attacking names to recognise.']],
 ['Young centres provide several development stories within the same club.','A coordinated forecheck can turn shared effort into retained possession. Watch the recovery rather than just the chase.','The first playoff run already supplies a recent example of the club’s ability to create shared memories.'],
 ['Who creates a dangerous chance when an opponent closes the middle?','Can the young centres earn more responsibility without losing defensive structure?','Does the second forechecker arrive in time to keep the puck?','Is possession reaching the slot or staying harmlessly around the outside?'],
 ['2023–24: 81 points, outside the playoff field.','2024–25: 76 points and another missed postseason.','2025–26: 79 points; the search for a sustained return continues.'],
 [['Jacob Melanson','Out indefinitely','The official update reported a vascular complication following an upper-body injury. No return timetable is asserted here.'],['Coverage note','Not a full medical ledger','See official team news for other current availability. Absence from this card does not mean a player is healthy.']],
 NHL+'/news/seattle-kraken-jacob-melanson-injury-status-update-october-10-2026','10–11 Oct 2026',
 [['Kraken official news',NHL+'/kraken/'],['Franchise record','https://records.nhl.com/sea/overview/season-by-season-record']])

glossary_text='''
AHL|The main professional development league below the NHL; affiliates help develop and supply players.
Apple|Slang for an assist.
Backcheck|Coming back toward your own goal to disrupt an opponent’s attack.
Bar down|A shot that hits the underside of the crossbar and goes in.
Beauty|Hockey slang for an admired player or person; context does the work.
Bench minor|A minor penalty assessed to a team or bench, such as too many players.
Blue line|One of the two lines dividing the rink into three zones; central to offside.
Boards|The wall around the playing surface.
Breakaway|An attacker has a clear path toward the goalie without a defender between them.
Breakout|Moving possession out of the defensive zone with useful support.
Butterfly|A goalie technique using the pads low while the knees are down.
Cap hit|The contract value counted for salary-cap purposes, which can differ from cash paid that year.
Celly|Slang for a celebration.
Centre|A forward with substantial responsibilities through the middle and often on faceoffs.
Change on the fly|Replacing players while play continues.
Chirp|A verbal jab or taunt.
Clapper|Slang for a slap shot.
Controlled entry|Crossing into the attacking zone while keeping possession, by carry or pass.
Corsi|All shot attempts: on target, missed and blocked. Often used as a possession proxy.
Crease|The marked area immediately around the goal.
Cycle|Keeping possession through movement and exchanges, often along the boards.
Delayed offside|Attackers may clear the attacking zone before resuming pressure, avoiding a whistle in eligible circumstances.
Delayed penalty|A signalled penalty where the official waits for the offending team to gain possession before stopping play, subject to rule details.
Depth|Useful contributors beyond the most prominent players, including injury cover and specialist roles.
Deke|A deceptive movement intended to make an opponent commit the wrong way.
Double minor|Two minor-penalty segments, often described as four minutes.
Dump and chase|Sending the puck behind the defence and trying to recover it.
Empty net|A goalie has been removed, often for an extra attacking skater late in a game.
Even strength|The teams have equal numbers of skaters; five-on-five is the common situation.
Expected goals|A model’s estimated scoring probability for chances, summed over shots; definitions differ by model.
Faceoff|The official drops the puck to restart play between opposing players.
Fenwick|Shot attempts excluding blocked shots.
Five-hole|The opening between a goalie’s legs.
Forecheck|Pressure aimed at recovering the puck in the opponent’s zone.
Gap control|A defender’s management of distance from an attacker, balancing pressure with protection against being beaten.
Games in hand|A team has played fewer games than a comparison team, leaving opportunities rather than guaranteed points.
GAA|Goals-against average: goals allowed per 60 minutes of goalie playing time.
Give-and-go|Pass, move into a new position and receive the return pass.
Gordie Howe hat trick|Informal term for a goal, assist and fight in one game.
Hat trick|Three goals by the same player in one game.
Healthy scratch|A player not selected to dress despite not being listed out injured.
High-danger chance|A provider-defined category for threatening opportunities; check the definition rather than assuming all sites agree.
Icing|Broadly, an eligible long clearance from behind centre beyond the opposing goal line; exceptions and hybrid-race judgments apply.
IR|Injured reserve: a roster designation, not a diagnosis or certain return date.
LTIR|Long-term injured reserve; cap relief and eligibility follow specific rules, rather than simply deleting a contract.
Matchup|The set of players deployed against a particular opposing group.
Natural hat trick|Three consecutive goals by one player without another player scoring between them.
Neutral zone|The middle region between the blue lines.
Odd-man rush|An attack with more attackers than immediately available defenders, such as two-on-one.
Offside|An attacking-zone entry violates the blue-line entry requirements; commonly an attacker gets in before the puck.
One-timer|A shot taken directly from a pass without first settling the puck.
OTL|Overtime loss in the standings column, including shootout losses; worth one point.
PDO|On-ice shooting percentage plus save percentage; a clue about percentages, not a guarantee of regression to one exact value.
Penalty kill|The structure and play used while shorthanded.
Pinch|A defenceman moves deeper to pressure or retain the puck, requiring cover behind him.
Playmaker|A player especially associated with creating opportunities for teammates.
Plus-minus|A context-sensitive count for certain goals while a skater is on the ice; weak as a stand-alone defensive verdict.
Point|Can mean a scoring point, a standings point, or a location near the attacking blue line. Context matters.
Points percentage|Standings points earned divided by the maximum available from games played.
Power play|A numerical skating advantage created by penalties.
Protected pick|A traded draft selection with conditions on when or whether it transfers.
Rebound control|A goalie’s management of where the puck goes after a save.
Regulation|The scheduled three periods before any overtime or shootout.
Restricted free agent|A player whose original team retains specified rights under eligibility and contract rules.
Saucer pass|A pass lifted so the puck travels above sticks or obstacles and settles for a receiver.
Screen|An obstruction of the goalie’s view of the puck.
Shift|One continuous stint of playing time before a skater goes to the bench.
Shorthanded|Playing with fewer skaters because of penalties.
Shutdown role|An assignment focused on limiting dangerous opponents.
Slot|The dangerous central attacking area in front of goal.
Special teams|Power-play and penalty-killing units and performance.
Stick lift|Lifting an opponent’s stick to prevent a play or recover the puck, within the rules.
Stretch pass|A long outlet intended to move the attack quickly up the ice.
Takeaway|A credited recovery from an opponent; scorer judgments and context affect counts.
Top six / bottom six|The first two and latter two forward lines, respectively; roles vary beyond the label.
Trapezoid|The marked area behind the net relevant to where goalies may play the puck.
Two-way player|A player contributing to attacking and defending.
Unrestricted free agent|An eligible player free to sign with another club, subject to league rules.
Waivers|A process allowing other clubs to claim certain players before a roster assignment or other eligible move.
Weak side|The side away from the puck; a place to look for an overlooked passing option.
Wild card|One of the conference playoff places outside the top three in each division.
Winger|A forward starting on the left or right, with responsibilities that extend well beyond the boards.
Wraparound|An attempt to carry the puck from behind the net around the post into goal.
Wrist shot|A shooting technique using a sweeping wrist action rather than a large slap-shot windup.
Zone exit|Getting the puck out of the defensive zone; quality depends on whether useful possession survives.
'''
glossary=[dict(term=line.split('|')[0],definition=line.split('|')[1]) for line in glossary_text.strip().splitlines()]
quiz=[
 ['What does five-on-five count?',['Skaters, excluding goalies','Everyone including goalies','Only forwards'],0,'Each team normally has five skaters and a goalie.'],
 ['A team has 20 wins, 10 regulation losses and 5 overtime losses. How many points?',['40','45','50'],1,'Two per win plus one per overtime or shootout loss: 45.'],
 ['A winger chips the puck deep while his line changes. What should you check?',['Whether the placement made the change safe','Whether every dump-in is bad','Only how fast the winger skates'],0,'Territory, recovery and timing matter; a safe change can be the purpose.'],
 ['Why might a quiet chest save be impressive?',['The shot must have been easy','The goalie may have read and positioned perfectly','Only diving saves require skill'],1,'Good anticipation can remove the need for a spectacular recovery.'],
 ['Does a high point total fully measure a player?',['Yes','No; opportunity, role and defence need context','Only for defencemen'],1,'Production matters but is not a complete player evaluation.'],
 ['Which team is your Canadiens’ great recurring historical rival?',['Boston Bruins','Seattle Kraken','Anaheim Ducks'],0,'Boston is a central historical rival; Toronto is another major one.'],
 ['What should you do with a September injury report in mid-October?',['Assume nothing has changed','Check a newer game-day source','Treat roster presence as medical clearance'],1,'A dated report describes what was known then, not a permanent status.'],
 ['How many regular-season games per club in 2026–27?',['82','84','80'],1,'This schedule expanded to 84; the three prior seasons in the tables had 82.'],
 ['If a defenceman pinches, what is the next useful place to look?',['Who covers behind him','The crowd reaction','Only whether he is tall'],0,'Support determines how much risk the team has accepted.'],
 ['Who is Ottawa’s captain in this snapshot?',['Brady Tkachuk','Thomas Chabot','Tim Stützle'],1,'Chabot was named captain in September 2026; old guides can mislead.'],
 ['Are the Wild the same franchise as the North Stars?',['Yes','No','Only in playoff games'],1,'The North Stars moved to Dallas; the Wild began as an expansion team in 2000.'],
 ['Which title belongs to Seattle’s earlier Metropolitans, rather than the Kraken?',['1917 Stanley Cup','2023 Stanley Cup','2024 Stanley Cup'],0,'City history and current-franchise records are different things.'],
 ['What happens after a power-play goal during an ordinary single minor?',['The minor generally ends','The penalty always continues five minutes','Both teams lose a player'],0,'That is the ordinary minor case; majors, double minors and overlapping calls differ.'],
 ['What is the weak side?',['The side away from the puck','The losing team’s bench','The left half of every rink'],0,'It is a moving relationship to the puck, not a permanent geographical side.'],
 ['Why compare points percentage?',['It accounts for games played','It measures shot speed','It predicts the Cup winner'],0,'Different teams may have played different numbers of games.'],
 ['What does a healthy scratch mean?',['Not selected to dress despite no listed injury','Guaranteed to start','Retired'],0,'Selection and medical availability are different questions.'],
 ['What should expected goals help you do?',['Ask better questions about chance quality','Declare the real score invalid','Ignore the goalie'],0,'It is a model estimate with assumptions, not an alternate official result.'],
 ['A team loses after creating good chances. What follows?',['It must have played badly','It may have played well; examine context','The coach must be fired'],1,'Outcomes and repeatable process overlap, but they are not identical.']]

sources=[['Official NHL video rulebook','https://www.nhl.com/info/video-rulebook'],['2026–27 schedule and 84-game format','https://www.nhl.com/news/nhl-stats-pack-2026-27-regular-season-schedule'],['NHL collective bargaining agreement details','https://www.nhl.com/news/nhl-new-collective-bargaining-agreement-details'],['Stanley Cup champions','https://www.nhl.com/news/topic/nhl-awards/nhl-stanley-cup-champions-winners-complete-list-287705398'],['Official NHL statistics','https://www.nhl.com/stats/'],['Official team summary data','https://api.nhle.com/stats/rest/en/team/summary?isAggregate=false&isGame=false&limit=100&cayenneExp=seasonId%3E%3D20232024%20and%20seasonId%3C%3D20252026%20and%20gameTypeId%3D2%20and%20(teamId%3D8%20or%20teamId%3D30%20or%20teamId%3D5%20or%20teamId%3D9%20or%20teamId%3D55)']]
histories={
 'MIN':[['Kirill Kaprizov','2025 lower-body surgery','Surgery announced 28 January 2025. Historical context; not a current absence.','https://www.nhl.com/news/minnesota-wild-kirill-kaprizov-injury-status-lower-body']],
 'PIT':[['Kris Letang','2022 stroke and return','Stroke reported in November 2022; returned in December. Historical context, not current status.','https://www.nhl.com/penguins/news/letang-returns-to-the-lineup-less-than-two-weeks-after-stroke-338647424'],['Evgeni Malkin','2021 knee surgery','Recovery affected the start of 2021–22. A historical interruption, not a current injury label.','https://www.nhl.com/news/evgeni-malkin-injury-status-326275352']],
 'OTT':[['Linus Ullmark','2024–25 back injury','Absent after 22 December 2024; back issue reported in January 2025. Historical, not current status.','https://www.nhl.com/news/linus-ullmark-out-week-to-week-with-back-injury-for-ottawa-senators']],
 'SEA':[['Jordan Eberle','2024 pelvic surgery','Surgery reported in November 2024. Historical context; not a claim of current unavailability.','https://www.nhl.com/news/kraken-jordan-eberle-out-3-months-after-pelvis-surgery']]
}
availability_updates={
 'MIN':('13 Oct 2026','https://www.nhl.com/news/minnesota-wild-winnipeg-jets-game-preview-october-13-2026',[
 ['Marcus Foligno','Mid body','Listed injured in the cited report.'],['Nick Foligno','Upper body','Listed injured.'],['Brock Faber','Skull fracture','Listed injured.'],['Filip Gustavsson','Lower body','Listed injured.'],['Nico Sturm','Upper body','Listed injured.']]),
 'PIT':('13 Oct 2026','https://www.nhl.com/news/pittsburgh-penguins-chicago-blackhawks-game-preview-october-13-2026',[
 ['Justin Brazeau','Lower body','Listed injured in the cited report.'],['Ryan Graves','Knee','Listed injured.'],['Trevor van Riemsdyk','Lower body','Listed injured.']]),
 'OTT':('13 Oct 2026','https://www.nhl.com/news/st-louis-blues-ottawa-senators-game-preview-october-13-2026',[
 ['Jake Sanderson','Undisclosed','Listed injured.'],['Artem Zub','Knee','Listed injured.'],['William Eklund','Ankle','Listed injured.'],['Kurtis MacDermid','Upper body','Listed injured.'],['Cameron Crotty','Undisclosed','Listed injured.'],['Nikolas Matinpalo','Upper body','Listed injured.']])
}
for t in teams:
    if t['abbr'] in availability_updates:
        date,url,items=availability_updates[t['abbr']]
        t['injuryDate']=date;t['injurySource']=url;t['injuries']=items
for t in teams:
    for n,inj,note,url in histories.get(t['abbr'],[]):
        t['injuries'].append(['History · '+n,inj,note])
        t['sources'].append([n+' · injury history',url])
hebrew_rows=json.loads((ROOT/'glossary-he.json').read_text(encoding='utf-8'))
translations={row[0]:row for row in hebrew_rows}
for entry in glossary:
    row=translations[entry['term']]
    entry.update(hebrew=row[1],hebrewDefinition=row[2])
known={entry['term'] for entry in glossary}
for row in hebrew_rows:
    if row[0] not in known:
        glossary.append(dict(term=row[0],definition=row[3],hebrew=row[1],hebrewDefinition=row[2]))
glossary.sort(key=lambda entry:entry['term'].casefold())
quick_rules=json.loads((ROOT/'quick-rules.json').read_text(encoding='utf-8'))
data=dict(date='15 October 2026',statsDate='14 October 2026',version='2026-10-15.2',lessons=lessons,teams=teams,glossary=glossary,quickRules=quick_rules,quiz=quiz,sources=sources)
(OUT/'data.json').write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
words=sum(len(' '.join(l['paragraphs']).split()) for l in lessons)
print(f'Built {len(lessons)} reading chapters, {words:,} words, {len(glossary)} glossary entries, {sum(len(t["roster"]) for t in teams)} roster entries and {len(quiz)} quiz questions.')
