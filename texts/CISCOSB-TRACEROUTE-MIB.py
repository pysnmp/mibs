#
# PySNMP MIB module CISCOSB-TRACEROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSB-TRACEROUTE-MIB
# Source digest sha256:8fbb827780da4fca4a12eda2c09c066f5cfc7607659179c657a03b08c70930e4
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlTraceRoute = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81))
rlTraceRoute.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlTraceRoute.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlTraceRoute.setLastUpdated('2007-01-02 00:00')
if mibBuilder.loadTexts: rlTraceRoute.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlTraceRoute.setContactInfo('Postal: 170 West Tasman Drive\n                San Jose , CA 95134-1706\n                USA\n\n                \n                Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlTraceRoute.setDescription('This private MIB module defines TRACE ROUTE private MIBs.')
rlTraceRouteMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setDescription("MIB's version, the current version is 1.")
rlTraceRouteWebLastTestName = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTraceRouteWebLastTestName.setStatus('current')
if mibBuilder.loadTexts: rlTraceRouteWebLastTestName.setDescription('The last index of Traceroute WEB requests. Used to configure traceRouteCtlTestName by WEB user.')
mibBuilder.exportSymbols("CISCOSB-TRACEROUTE-MIB", PYSNMP_MODULE_ID=rlTraceRoute, rlTraceRoute=rlTraceRoute, rlTraceRouteMibVersion=rlTraceRouteMibVersion, rlTraceRouteWebLastTestName=rlTraceRouteWebLastTestName)
