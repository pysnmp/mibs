#
# PySNMP MIB module CISCO-ATM-CONN-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCO-ATM-CONN-INFO-MIB
# Source digest sha256:1ef13ab0f546895463b5f1d960eeb2c26a813b3296d341cc002e02ea018ea4a4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmConnInfoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9999))
ciscoAtmConnInfoMIB.setRevisions(('2003-06-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setRevisionsDescriptions(('Initial version of the MIB.',))
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setLastUpdated('2003-06-16 00:00')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setContactInfo('       Cisco Systems\n                         Customer Service\n\n                 Postal: 170 W Tasman Drive\n                         San Jose, CA  95134\n                         USA\n\n                         Tel: +1 800 553-NETS\n\n                 E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIB.setDescription('The MIB module for providing the parameters \n                  configured on an ATM interface.\n                  Terminologies used:\n                  SVC  : Switched Virtual Channel\n                  SPVC : Soft Permanent Virtual Circuit\n                  SPVP : Soft Permanent Virtual Path\n                  SVPC : Switched Virtual Path Connection\n                  DAX  : Connection with endpoints on the same \n                         ATM switch\n                  P2p  : Point-to-point connection\n                  P2mp : Point-to-multi-point connection\n                  Root : The root of point-to-multipoint connection,\n                         which is associated with a VPI/VCI\n                  Leaf : Usually one point-to-multipoint connection\n                         consists of one root and one or more leaves. \n                         Leaf is the branch point for point \n                         to multipoint connection that is \n                         associated with a VPI/VCI\n                  Party: One or more party is associated with each \n                         leaf, all parties are associated with \n                         the same VPI/VCI that its leaf belongs to\n                  \n                  Source           Via Node           Destination\n                  -------          -------            -------\n                 A|     |B        C|     |D          E|     |F\n                --+-----+----------+-----+------------+-----+--\n                  |     |          |     |            |     |     \n                  -------          -------            -------\n                  Each active connection has two terminating \n                  endpoints. \n                  In the above diagram, Endpoints A and F are \n                  terminating.\n                  Of these the master endpoint of the connection \n                  initiates the routing of the call and is \n                  considered the calling party. The slave endpoint\n                  is the called party which receives calls and is \n                  the destination of a call.\n                  Any endpoints that are created either on Via nodes \n                  or on the node with the terminating endpoint in \n                  order to have a complete connections between \n                  endpoints A and F are said to be intermediate \n                  endpoints. In the above diagram, endpoints B, C, \n                  D and E are intermediate endpoints.\n                  ')
caciMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 0))
caciMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1))
caciAtmConnInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1))
caciIfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1))
caciP2pConns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2))
caciP2pEndpoints = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3))
caciP2pIntEndpoints = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4))
caciP2mpConns = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5))
caciGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6))
class CaciGeneralConnEPCategory(TextualConvention, Integer32):
    description = 'General category for connection or endpoint types \n         supported on the switch.\n         caciP2p    : Point to point connection\n         caciP2mpR  : Point to multi point root connection\n         caciP2mpL  : Point to multi point leaf connection\n         caciP2mpPty: Point to multi point party connection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciP2p", 1), ("caciP2mpR", 2), ("caciP2mpL", 3), ("caciP2mpPty", 4))

class CaciP2pConnCategory(TextualConvention, Integer32):
    description = 'The connection category.\n         caciP2pSvcc : Point to point Svc connection\n         caciP2pSvpc : Point to point Svpc connection\n         caciP2pSpvcD: Point to point Spvc DAX connection\n         caciP2pSpvpD: Point to point Spvp DAX connection\n         caciP2pSpvcR: Point to point SPVC Routed connection\n         caciP2pSpvpR: Point to point Spvp Routed connection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("caciP2pSvcc", 1), ("caciP2pSvpc", 2), ("caciP2pSpvcD", 3), ("caciP2pSpvpD", 4), ("caciP2pSpvcR", 5), ("caciP2pSpvpR", 6))

class CaciP2pEndpointCategory(TextualConvention, Integer32):
    description = 'The terminating endpoint category.\n        caciP2pSpvcRPEP : Point to point Spvc \n                          Routed Persistent endpoint\n        caciP2pSpvcRNPEP: Point to point Spvc \n                          Routed Non-persistent endpoint\n        caciP2pSpvpRPEP : Point to point Spvp \n                          Routed Persistent endpoint\n        caciP2pSpvpRNPEP: Point to point Spvp \n                          Routed Non-persistent endpoint\n        caciP2pSpvcDEP  : Point to point Spvc \n                          DAX endpoint\n        caciP2pSpvpDEP  : Point to point Spvp \n                          DAX endpoint'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("caciP2pSpvcRPEP", 1), ("caciP2pSpvcRNPEP", 2), ("caciP2pSpvpRPEP", 3), ("caciP2pSpvpRNPEP", 4), ("caciP2pSpvcDEP", 5), ("caciP2pSpvpDEP", 6))

class CaciP2pIntEndpointCategory(TextualConvention, Integer32):
    description = 'The intermediate endpoint category.\n         caciP2pSvccIntEP : Point to point Svc \n                            intermediate endpoint\n         caciP2pSvpcIntEP : Point to point Svpc \n                            intermediate endpoint\n         caciP2pSpvcRIntEP: Point to point Spvc Routed \n                            intermediate endpoint\n         caciP2pSpvpRIntEP: Point to point Spvp Routed \n                            intermediate endpoint'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciP2pSvccIntEP", 1), ("caciP2pSvpcIntEP", 2), ("caciP2pSpvcRIntEP", 3), ("caciP2pSpvpRIntEP", 4))

class CaciP2mpConnCategory(TextualConvention, Integer32):
    description = 'The point to multipoint connection category.\n         caciP2mpSvcRoot  : Point to multipoint Svc \n                            root connection\n         caciP2mpSvcLeaf  : Point to multipoint Svc \n                            leaf connection\n         caciP2mpSvcParty : Point to multipoint Svc \n                            party connection\n         caciP2mpSvpcRoot : Point to multipoint Svpc \n                            root connection\n         caciP2mpSvpcLeaf : Point to multipoint Svpc \n                            leaf connection\n         caciP2mpSvpcParty: Point to multipoint Svpc \n                            party connection\n         caciP2mpSpvcP    : Point to multipoint Spvc\n                            persistent connection\n         caciP2mpSpvcNP   : Point to multipoint Spvc\n                            non-persistent connection\n         caciP2mpSpvcAct  : Point to multipoint Spvc\n                            Active connection\n         caciP2mpSpvpP    : Point to multipoint Spvp\n                            persistent connection\n         caciP2mpSpvpNP   : Point to multipoint Spvp\n                            non-persistent connection\n         caciP2mpSpvpAct  : Point to multipoint Spvp\n                            active connection\n         caciP2mpSpvcPaP  : Point to multipoint Spvc\n                            party persistent connection\n         caciP2mpSpvcPaAct: Point to multipoint Spvc\n                            party active connection\n         caciP2mpSpvpPaP  : Point to multipoint Spvp\n                            party persistent connection\n         caciP2mpSpvpPaAct: Point to multipoint Spvp \n                            party active connection'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("caciP2mpSvcRoot", 1), ("caciP2mpSvcLeaf", 2), ("caciP2mpSvcParty", 3), ("caciP2mpSvpcRoot", 4), ("caciP2mpSvpcLeaf", 5), ("caciP2mpSvpcParty", 6), ("caciP2mpSpvcP", 7), ("caciP2mpSpvcNP", 8), ("caciP2mpSpvcAct", 9), ("caciP2mpSpvpP", 10), ("caciP2mpSpvpNP", 11), ("caciP2mpSpvpAct", 12), ("caciP2mpSpvcPaP", 13), ("caciP2mpSpvcPaAct", 14), ("caciP2mpSpvpPaP", 15), ("caciP2mpSpvpPaAct", 16))

class CaciATMEndpointCategory(TextualConvention, Integer32):
    description = 'The connection category.\n         caciTotalSpvc   : Total SPVC endpoints configured \n                           on the ATM switch\n         caciP2pTotalInt : Total intermediate endpoints\n                           configured on the ATM switch\n         caciTotalMaster : Total master endpoints configured\n                           on the ATM switch\n         caciTotalSlave  : Total slave endpoints configured\n                           on the ATM switch'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("caciTotalSpvc", 1), ("caciP2pTotalInt", 2), ("caciTotalMaster", 3), ("caciTotalSlave", 4))

caciP2pTotalConfConns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConfConns.setStatus('current')
if mibBuilder.loadTexts: caciP2pTotalConfConns.setDescription('This object specifies the total point to point\n                 connections that are configured on this ATM switch.')
caciP2pMaxPossibleConns = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pMaxPossibleConns.setStatus('current')
if mibBuilder.loadTexts: caciP2pMaxPossibleConns.setDescription('This object specifies the upper limit of the \n                 point to point and point to multipoint \n                 connections that are allowed to be configured\n                 on this ATM switch.')
caciMaxPossibleEndpoints = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciMaxPossibleEndpoints.setStatus('current')
if mibBuilder.loadTexts: caciMaxPossibleEndpoints.setDescription('This object specifies the upper limit of all the \n         possible endpoints that are allowed to be \n         configured on this ATM switch.')
caciGenericEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciGenericEndpointTable.setStatus('current')
if mibBuilder.loadTexts: caciGenericEndpointTable.setDescription('The table contains number of connection per \n         CaciATMEndpointCategory.')
caciGenericEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciATMEndpointCategory"))
if mibBuilder.loadTexts: caciGenericEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: caciGenericEndpointEntry.setDescription('An entry in the table specifying the number \n         of connections for the corresponding \n         CaciATMEndpointCategory.')
caciATMEndpointCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 1), CaciATMEndpointCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciATMEndpointCategory.setStatus('current')
if mibBuilder.loadTexts: caciATMEndpointCategory.setDescription('Endpoint category corresponding to \n         CaciATMEndpointCategory.')
caciTotalEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 6, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciTotalEndpoints.setStatus('current')
if mibBuilder.loadTexts: caciTotalEndpoints.setDescription('The total number of endpoints of \n         caciATMEndpointCategory configured \n         on this ATM switch.')
caciConnInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciConnInfoTable.setStatus('current')
if mibBuilder.loadTexts: caciConnInfoTable.setDescription('The Connection Statistics table. \n         This table has the number of connections per interface.')
caciConnInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-ATM-CONN-INFO-MIB", "caciGeneralConnEPCategory"))
if mibBuilder.loadTexts: caciConnInfoEntry.setStatus('current')
if mibBuilder.loadTexts: caciConnInfoEntry.setDescription('An entry in the caciConnInfoTable. \n         Each entry in ifTable with ifType \n         values: atm(37), atmLogical(80) or atmVirtual(149) \n         has an associated entry in this table.')
caciGeneralConnEPCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 1), CaciGeneralConnEPCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciGeneralConnEPCategory.setStatus('current')
if mibBuilder.loadTexts: caciGeneralConnEPCategory.setDescription('The general connection or endpoint category\n         on this ATM switch.')
caciNumUsedConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 1, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciNumUsedConns.setStatus('current')
if mibBuilder.loadTexts: caciNumUsedConns.setDescription('This object specifies the total number of used \n         connections of type caciGeneralConnEPCategory \n         on this interface.')
caciP2pConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pConnTable.setStatus('current')
if mibBuilder.loadTexts: caciP2pConnTable.setDescription('The table contains number of connection per \n         CaciP2pConnCategory.')
caciP2pConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pConnectionCategory"))
if mibBuilder.loadTexts: caciP2pConnEntry.setStatus('current')
if mibBuilder.loadTexts: caciP2pConnEntry.setDescription('An entry in the table specifying the number \n         of connections for the corresponding CaciP2pConnCategory.')
caciP2pConnectionCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 1), CaciP2pConnCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pConnectionCategory.setStatus('current')
if mibBuilder.loadTexts: caciP2pConnectionCategory.setDescription('The connection category.')
caciP2pTotalConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConns.setStatus('current')
if mibBuilder.loadTexts: caciP2pTotalConns.setDescription('The total number of P2p connections of type \n         CaciP2pConnCategory configured on this ATM switch.')
caciP2pEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pEndpointTable.setStatus('current')
if mibBuilder.loadTexts: caciP2pEndpointTable.setDescription('The table contains number of endpoints per \n         CaciP2pEndpointCategory.')
caciP2pEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pEndptCategory"))
if mibBuilder.loadTexts: caciP2pEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: caciP2pEndpointEntry.setDescription('An entry in the table specifying the number \n         of endpoints for the corresponding \n         CaciP2pEndpointCategory.')
caciP2pEndptCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 1), CaciP2pEndpointCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pEndptCategory.setStatus('current')
if mibBuilder.loadTexts: caciP2pEndptCategory.setDescription('The point to point endpoint category.')
caciP2pTotalConfEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 3, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalConfEndpoints.setStatus('current')
if mibBuilder.loadTexts: caciP2pTotalConfEndpoints.setDescription('The number of total P2p enpoints of type \n         CaciP2pEndpointCategory configured on this ATM switch.')
caciP2pIntEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pIntEndpointTable.setStatus('current')
if mibBuilder.loadTexts: caciP2pIntEndpointTable.setDescription('The table contains number of endpoints per \n         CaciP2pIntEndpointCategory.')
caciP2pIntEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2pIntEndptCategory"))
if mibBuilder.loadTexts: caciP2pIntEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: caciP2pIntEndpointEntry.setDescription('An entry in the table specifying the number \n         of endpoints for the corresponding \n         CaciP2pIntEndpointCategory.')
caciP2pIntEndptCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 1), CaciP2pIntEndpointCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2pIntEndptCategory.setStatus('current')
if mibBuilder.loadTexts: caciP2pIntEndptCategory.setDescription('The point to point intermediate endpoint category.')
caciP2pTotalIntEndpoints = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 4, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2pTotalIntEndpoints.setStatus('current')
if mibBuilder.loadTexts: caciP2pTotalIntEndpoints.setDescription('The total number of P2p intermediate enpoints of type \n         CaciP2pIntEndpointCategory present on this ATM switch.')
caciP2mpConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1), ).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2mpConnTable.setStatus('current')
if mibBuilder.loadTexts: caciP2mpConnTable.setDescription('The table contains number of connection per \n         CaciP2mpConnCategory.')
caciP2mpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1), ).setMaxAccess("notaccessible").setIndexNames((0, "CISCO-ATM-CONN-INFO-MIB", "caciP2mpConnectionCategory"))
if mibBuilder.loadTexts: caciP2mpConnEntry.setStatus('current')
if mibBuilder.loadTexts: caciP2mpConnEntry.setDescription('An entry in the table specifying the number \n         of connections for the corresponding \n         CaciP2mpConnCategory.')
caciP2mpConnectionCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 1), CaciP2mpConnCategory()).setMaxAccess("notaccessible")
if mibBuilder.loadTexts: caciP2mpConnectionCategory.setStatus('current')
if mibBuilder.loadTexts: caciP2mpConnectionCategory.setDescription('The point to multi point connection category.')
caciP2mpTotalConfConns = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9999, 1, 1, 5, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: caciP2mpTotalConfConns.setStatus('current')
if mibBuilder.loadTexts: caciP2mpTotalConfConns.setDescription('The total number of P2mp connections of type \n         CaciP2mpConnCategory configured on this ATM switch.')
ciscoAtmConnInfoMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2))
ciscoAtmConnInfoMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1))
ciscoAtmConnInfoMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2))
ciscoAtmConnInfoMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 1, 1)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "ciscoConnInfoConfMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoTotalConnsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoTotalEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pConnsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2pIntEndpointsMIBGroup"), ("CISCO-ATM-CONN-INFO-MIB", "ciscoP2mpConnsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmConnInfoMIBCompliance = ciscoAtmConnInfoMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmConnInfoMIBCompliance.setDescription('The Compliance statement for ciscoAtm management group.')
ciscoConnInfoConfMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 1)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciNumUsedConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoConnInfoConfMIBGroup = ciscoConnInfoConfMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoConnInfoConfMIBGroup.setDescription('Objects used for representing connection \n             statistical details about an interface.')
ciscoP2pConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 2)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pConnsMIBGroup = ciscoP2pConnsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2pConnsMIBGroup.setDescription('Objects used for representing the point to point \n         connections of a particular CaP2pConnCategory.')
ciscoP2pEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 3)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pEndpointsMIBGroup = ciscoP2pEndpointsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2pEndpointsMIBGroup.setDescription('Objects used for representing the point to point \n         endpoints of a particular CaP2pEndpointCategory.')
ciscoP2pIntEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 4)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalIntEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2pIntEndpointsMIBGroup = ciscoP2pIntEndpointsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2pIntEndpointsMIBGroup.setDescription('Objects used for representing the point to point \n         intermediate endpoints of a particular \n         CaP2pIntEndpointCategory.')
ciscoP2mpConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 5)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2mpTotalConfConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2mpConnsMIBGroup = ciscoP2mpConnsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoP2mpConnsMIBGroup.setDescription('Objects used for representing the point to multi point \n         connections of a particular CaP2mpConnCategory.')
ciscoTotalConnsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 6)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciP2pTotalConfConns"), ("CISCO-ATM-CONN-INFO-MIB", "caciP2pMaxPossibleConns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTotalConnsMIBGroup = ciscoTotalConnsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoTotalConnsMIBGroup.setDescription('Objects used for representing the total connections\n         on the ATM switch.')
ciscoTotalEndpointsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9999, 2, 2, 7)).setObjects(("CISCO-ATM-CONN-INFO-MIB", "caciMaxPossibleEndpoints"), ("CISCO-ATM-CONN-INFO-MIB", "caciTotalEndpoints"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTotalEndpointsMIBGroup = ciscoTotalEndpointsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoTotalEndpointsMIBGroup.setDescription('Objects used for representing the total endpoints \n         on the ATM switch.')
mibBuilder.exportSymbols("CISCO-ATM-CONN-INFO-MIB", CaciATMEndpointCategory=CaciATMEndpointCategory, CaciGeneralConnEPCategory=CaciGeneralConnEPCategory, CaciP2mpConnCategory=CaciP2mpConnCategory, CaciP2pConnCategory=CaciP2pConnCategory, CaciP2pEndpointCategory=CaciP2pEndpointCategory, CaciP2pIntEndpointCategory=CaciP2pIntEndpointCategory, PYSNMP_MODULE_ID=ciscoAtmConnInfoMIB, caciATMEndpointCategory=caciATMEndpointCategory, caciAtmConnInfo=caciAtmConnInfo, caciConnInfoEntry=caciConnInfoEntry, caciConnInfoTable=caciConnInfoTable, caciGeneralConnEPCategory=caciGeneralConnEPCategory, caciGeneric=caciGeneric, caciGenericEndpointEntry=caciGenericEndpointEntry, caciGenericEndpointTable=caciGenericEndpointTable, caciIfInfo=caciIfInfo, caciMIBNotifications=caciMIBNotifications, caciMIBObjects=caciMIBObjects, caciMaxPossibleEndpoints=caciMaxPossibleEndpoints, caciNumUsedConns=caciNumUsedConns, caciP2mpConnEntry=caciP2mpConnEntry, caciP2mpConnTable=caciP2mpConnTable, caciP2mpConnectionCategory=caciP2mpConnectionCategory, caciP2mpConns=caciP2mpConns, caciP2mpTotalConfConns=caciP2mpTotalConfConns, caciP2pConnEntry=caciP2pConnEntry, caciP2pConnTable=caciP2pConnTable, caciP2pConnectionCategory=caciP2pConnectionCategory, caciP2pConns=caciP2pConns, caciP2pEndpointEntry=caciP2pEndpointEntry, caciP2pEndpointTable=caciP2pEndpointTable, caciP2pEndpoints=caciP2pEndpoints, caciP2pEndptCategory=caciP2pEndptCategory, caciP2pIntEndpointEntry=caciP2pIntEndpointEntry, caciP2pIntEndpointTable=caciP2pIntEndpointTable, caciP2pIntEndpoints=caciP2pIntEndpoints, caciP2pIntEndptCategory=caciP2pIntEndptCategory, caciP2pMaxPossibleConns=caciP2pMaxPossibleConns, caciP2pTotalConfConns=caciP2pTotalConfConns, caciP2pTotalConfEndpoints=caciP2pTotalConfEndpoints, caciP2pTotalConns=caciP2pTotalConns, caciP2pTotalIntEndpoints=caciP2pTotalIntEndpoints, caciTotalEndpoints=caciTotalEndpoints, ciscoAtmConnInfoMIB=ciscoAtmConnInfoMIB, ciscoAtmConnInfoMIBCompliance=ciscoAtmConnInfoMIBCompliance, ciscoAtmConnInfoMIBCompliances=ciscoAtmConnInfoMIBCompliances, ciscoAtmConnInfoMIBConformance=ciscoAtmConnInfoMIBConformance, ciscoAtmConnInfoMIBGroups=ciscoAtmConnInfoMIBGroups, ciscoConnInfoConfMIBGroup=ciscoConnInfoConfMIBGroup, ciscoP2mpConnsMIBGroup=ciscoP2mpConnsMIBGroup, ciscoP2pConnsMIBGroup=ciscoP2pConnsMIBGroup, ciscoP2pEndpointsMIBGroup=ciscoP2pEndpointsMIBGroup, ciscoP2pIntEndpointsMIBGroup=ciscoP2pIntEndpointsMIBGroup, ciscoTotalConnsMIBGroup=ciscoTotalConnsMIBGroup, ciscoTotalEndpointsMIBGroup=ciscoTotalEndpointsMIBGroup)
