#
# PySNMP MIB module CORERO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/corero/CORERO-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:16:51 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibIdentifier, Counter64, NotificationType, Gauge32, enterprises, Bits, ObjectIdentity, iso, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Counter64", "NotificationType", "Gauge32", "enterprises", "Bits", "ObjectIdentity", "iso", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
corero = ModuleIdentity((1, 3, 6, 1, 4, 1, 41036))
corero.setRevisions(('2017-06-16 00:00', '2014-04-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: corero.setRevisionsDescriptions(('Updated contact info.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: corero.setLastUpdated('201706160000Z')
if mibBuilder.loadTexts: corero.setOrganization('Corero Network Security')
if mibBuilder.loadTexts: corero.setContactInfo('        Corero Support\n             E-mail: support.portal@corero.com')
if mibBuilder.loadTexts: corero.setDescription('Corero Management Server MIB.')
coreroRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 1))
if mibBuilder.loadTexts: coreroRegistrations.setStatus('current')
if mibBuilder.loadTexts: coreroRegistrations.setDescription('This module defines the enterprises OID for Corero Network Security.')
coreroProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 2))
if mibBuilder.loadTexts: coreroProducts.setStatus('current')
if mibBuilder.loadTexts: coreroProducts.setDescription('A registration point under which all Corero AGENT-CAPABILIITES\n         definitions (and therefore values of sysObjectId) are defined.')
mibBuilder.exportSymbols("CORERO-MIB", corero=corero, coreroRegistrations=coreroRegistrations, coreroProducts=coreroProducts, PYSNMP_MODULE_ID=corero)
