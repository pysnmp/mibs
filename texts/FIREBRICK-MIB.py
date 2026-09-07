#
# PySNMP MIB module FIREBRICK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source FIREBRICK-MIB
# Source digest sha256:4368d6fb3fd1a4f49f40039d85bec3fbf88667b3f4dc1b9ccae47fc498509b30
# Produced by pysmi-2.3.0
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Counter64, Gauge32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, enterprises, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "enterprises", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
firebrick = ModuleIdentity((1, 3, 6, 1, 4, 1, 24693))
firebrick.setRevisions(('2020-04-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: firebrick.setRevisionsDescriptions(('Initial version of this MIB module',))
if mibBuilder.loadTexts: firebrick.setLastUpdated('2020-04-06 00:00')
if mibBuilder.loadTexts: firebrick.setOrganization('Andrews & Arnold Limited')
if mibBuilder.loadTexts: firebrick.setContactInfo('Andrews & Arnold\n        Unit 1&2, Enterprise Court\n        Bracknell, Berkshire, RG12 1QS\n        United Kingdom\n\n        Tel: +44 3333 400 999\n        Email: support@aa.net.uk')
if mibBuilder.loadTexts: firebrick.setDescription('This is a MIB Module for monitoring the Firebrick-specific structures\n        for general system features.')
firebrickNewStyle = MibIdentifier((1, 3, 6, 1, 4, 1, 24693, 100))
mibBuilder.exportSymbols("FIREBRICK-MIB", PYSNMP_MODULE_ID=firebrick, firebrick=firebrick, firebrickNewStyle=firebrickNewStyle)
