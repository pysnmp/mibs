#
# PySNMP MIB module CISCOSMB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source CISCOSMB-MIB
# Source digest sha256:5d518e8c863146cb6cc2e037fc076742f1385009135f1516df7fd030ea626503
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9))
cisco.setRevisions(('2010-10-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cisco.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: cisco.setLastUpdated('2010-10-31 00:00')
if mibBuilder.loadTexts: cisco.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cisco.setContactInfo('Postal: 170 West Tasman Drive\n\t\tSan Jose , CA 95134-1706\n\t\tUSA\n\n\t\t\n\t\tWebsite:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: cisco.setDescription('The private MIB module definition for CISCOSB private MIB tree.')
otherEnterprises = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6))
ciscosb = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1))
switch001 = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
rndMib = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 6, 1, 101))
mibBuilder.exportSymbols("CISCOSMB-MIB", PYSNMP_MODULE_ID=cisco, cisco=cisco, ciscosb=ciscosb, otherEnterprises=otherEnterprises, rndMib=rndMib, switch001=switch001)
