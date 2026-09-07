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
if mibBuilder.loadTexts: rlTraceRoute.setLastUpdated('2007-01-02 00:00')
if mibBuilder.loadTexts: rlTraceRoute.setOrganization('Cisco Systems, Inc.')
rlTraceRouteMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTraceRouteMibVersion.setStatus('current')
rlTraceRouteWebLastTestName = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 81, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTraceRouteWebLastTestName.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-TRACEROUTE-MIB", PYSNMP_MODULE_ID=rlTraceRoute, rlTraceRoute=rlTraceRoute, rlTraceRouteMibVersion=rlTraceRouteMibVersion, rlTraceRouteWebLastTestName=rlTraceRouteWebLastTestName)
